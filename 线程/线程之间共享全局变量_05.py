#  coding:utf-8
import threading
import time

g_list = []


def add_data():
    for i in range(5):
        g_list.append(i)
        print('add:', i)
        time.sleep(0.1)
    print('添加完成：', g_list)


def read_data():
    print('读取数据：', g_list)


if __name__ == '__main__':
    add_thread = threading.Thread(target=add_data)
    read_thread = threading.Thread(target=read_data)
    add_thread.start()
    # 让当前线程(主线程)等待添加数据的子线程执行完成后代码再继续执行
    add_thread.join()
    read_thread.start()
