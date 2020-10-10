#  coding:utf-8
import multiprocessing
import time

# 进程之间执行是无序的，是由操作系统调度进程来决定的
def task():
    time.sleep(1)
    print(multiprocessing.current_process())


if __name__ == '__main__':
    # 循环创建多个子进程
    for i in range(30):
        sub_process = multiprocessing.Process(target=task)
        sub_process.start()
