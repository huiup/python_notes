#  coding:utf-8
import threading
import time

# 互斥锁:对共享数据进行锁定﹐保证同—时刻只能有一个线程去操作
# 互斥锁可以保证同一时刻只有一个线程去执行﹐能够保证全局变量的数据没有问题

g_num = 0

# 创建互斥锁
lock = threading.Lock()


def task1():
    # 上锁
    lock.acquire()
    for i in range(1000000):
        global g_num  # 声明要修改全局变量的内存地址
        g_num += 1
    print('task1:', g_num)
    # 释放锁
    lock.release()


def task2():
    # 上锁
    lock.acquire()
    for i in range(1000000):
        global g_num  # 声明要修改全局变量的内存地址
        g_num += 1
    print('task2:', g_num)
    # 释放锁
    lock.release()


if __name__ == '__main__':
    first_thread = threading.Thread(target=task1)
    second_thread = threading.Thread(target=task2)
    first_thread.start()
    second_thread.start()
