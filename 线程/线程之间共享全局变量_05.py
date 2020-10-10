#  coding:utf-8
import threading

alist = []


def add_data():
    for i in range(5):
        alist.append(i)
        print(i)
    print('添加完成：', alist)


if __name__ == '__main__':
    add_thread = threading.Thread(target=add_data())
    add_thread.start()
