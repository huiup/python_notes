#  coding:utf-8
import threading
import time

# 线程等待和互斥锁都是把多任务改成单任务去执行，保证了数据的准确性﹐但是执行性能会下降

g_num = 0


def task1():
    for i in range(1000000):
        global g_num  # 声明要修改全局变量的内存地址
        g_num += 1
    print('task1:', g_num)


def task2():
    for i in range(1000000):
        global g_num  # 声明要修改全局变量的内存地址
        g_num += 1
    print('task2:', g_num)


if __name__ == '__main__':
    first_thread = threading.Thread(target=task1)
    second_thread = threading.Thread(target=task2)
    first_thread.start()
    # 解决方法：--->线程同步
    # 1.钱程等待﹐让第一个线程先执行﹐然后在让第二个线程再执行﹐保证数据不会有问题
    first_thread.join()  # 主线程等待第一个子线程执行完成以后代码再继续往下执行
    second_thread.start()
    # 2.互斥锁:对共享数据进行锁定﹐保证同—时刻只能有一个线程去操作
