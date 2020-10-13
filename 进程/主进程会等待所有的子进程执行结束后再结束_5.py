#  coding:utf-8

import multiprocessing
import time


def task():
    # for i in range(10):
    while True:
        print('任务执行中！！！')
        time.sleep(0.2)


if __name__ == '__main__':
    sub_process = multiprocessing.Process(target=task)
    # sub_process.daemon = True# 1.把子进程设置成为守护主进程(daemon)﹐以后主进程退出子进程直接销毁
    sub_process.start()
    time.sleep(0.7)
    # sub_process.terminate()# 2.主进程退出之前先让子进程销毁
    print('over')


