#  coding:utf-8
import threading
import time

# 线程间执行是无序的，是由cpu调度来决定的

def task():
    time.sleep(1)
    print(threading.current_thread())


if __name__ == '__main__':
    # 循环创建大量线程
    for i in range(30):
        sub_thread = threading.Thread(target=task)
        sub_thread.start()
