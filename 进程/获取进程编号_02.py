# coding:utf-8
import multiprocessing
import time
import os


# 创建子进程（自己手动创建的进程称为子进程)
def dance():
    # 获取当前进程编号(子进程)
    dance_process_id = os.getpid()
    print('dance_process_id:', dance_process_id, multiprocessing.current_process())
    print('dance_process的父进程编号：', os.getppid())
    for i in range(3):
        print('跳舞中。。。')
        time.sleep(0.2)


def sing():
    sing_process_id = os.getpid()
    print('sing_process_id:', sing_process_id, multiprocessing.current_process())
    print('sing_process的父进程编号：', os.getppid())
    for i in range(3):
        print('唱歌中。。。')
        time.sleep(0.2)
        # 根据进程编号强制杀死指定进程
        # os.kill(sing_process_id, 9)


if __name__ == '__main__':
    # 获取当前进程的编号(主进程)
    main_process_id = os.getpid()
    # 获取当前进程对象：multiprocessing.current_process()
    print('main_process_id:', main_process_id, multiprocessing.current_process())

    # 子进程
    dance_process = multiprocessing.Process(target=dance, name='dance_process')
    sing_process = multiprocessing.Process(target=sing, name='sing_process')
    dance_process.start()
    sing_process.start()
