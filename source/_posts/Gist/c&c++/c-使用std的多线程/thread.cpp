
#include <iostream>
#include <conio.h>
#include <thread>
#include <mutex>

int				g_cnt = 0;
std::mutex		g_mtx;					// 互斥量

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
		thrd_child[k] = new std::thread(tfunc,k);    // 按值传递参数k
		//thrd_child[k]->join();		// 阻塞当前线程，直至 *this 所标识的线程完成其执行。
		thrd_child[k]->detach();		// 从 thread 对象分离执行的线程，允许执行独立地持续。
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

