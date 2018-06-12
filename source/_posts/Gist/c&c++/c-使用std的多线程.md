---
title: 'c/c++:使用std的多线程'
categories:
  - Gist
mathjax: false
tags:
  - c/c++
date: 2018-01-25 10:26:09
---

> File : [thread.cpp](thread.cpp) *(直接右键另存为下载)*
> Type : c++
> Brief : 使用std的多线程类

<!-- more -->

---

```cpp
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


```
