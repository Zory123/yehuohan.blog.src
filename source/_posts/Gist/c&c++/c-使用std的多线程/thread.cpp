
#include <iostream>
#include <conio.h>
#include <thread>
#include <mutex>

int				g_cnt = 0;
std::mutex		g_mtx;					// ������

void tfunc(int k)
{
	std::this_thread::sleep_for(std::chrono::milliseconds(10));

	g_mtx.lock();
	g_cnt++;
    std::cout << "k: " << k << "		" << "g_cnt: " << g_cnt << std::endl;
	g_mtx.unlock();
}

int main()
{
    std::thread* thrd_child[10];

	int k = 0;
	while(k < 10)
	{
		thrd_child[k] = new std::thread(tfunc,k);    // ��ֵ���ݲ���k
		//thrd_child[k]->join();		// ������ǰ�̣߳�ֱ�� *this ����ʶ���߳������ִ�С�
		thrd_child[k]->detach();		// �� thread �������ִ�е��̣߳�����ִ�ж����س�����
		k++;
	}

	while(1)
	{
		char ch = getch();

		if('q' == ch || 27 == ch)
			break;
	};
	return 0;
}

