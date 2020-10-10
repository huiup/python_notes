#  coding:utf-8

import threading
import time


def task():
    while True:
        print('任务执行中！！！')
        time.sleep(0.3)


if __name__ == '__main__':
    # sub_thread = threading.Thread(target=task, daemon=True)  # 1.daemon=True表示创建的子线程守护主线程·主线程退出子线程直接销毁
    sub_thread = threading.Thread(target=task)
    sub_thread.setDaemon(True)# 2.把子线程设置成为守护主线程
    sub_thread.start()
    time.sleep(1)
    print('over!')
