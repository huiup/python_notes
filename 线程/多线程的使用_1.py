#  coding:utf-8

import threading
import time


def sing():
    # 获取当前线程
    current_thread = threading.current_thread()
    print('sing_thread:', current_thread)
    for i in range(3):
        print('唱歌中。。。')
        time.sleep(0.3)


def dance():
    # 获取当前线程
    current_thread = threading.current_thread()
    print('dance_thread:', current_thread)
    for i in range(3):
        print('跳舞中。。。')
        time.sleep(0.3)


if __name__ == '__main__':
    main_thread = threading.current_thread()
    print('main_thread:', main_thread)

    sing_thread = threading.Thread(target=sing, name='sing_thread')
    dance_thread = threading.Thread(target=dance, name='dance_thread')
    sing_thread.start()
    dance_thread.start()
