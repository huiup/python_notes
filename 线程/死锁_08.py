#  coding:utf-8

import threading

# 死锁:一直等待对方释放锁的情景叫做死锁

lock = threading.Lock()


def get_value(index):
    # 上锁
    lock.acquire()
    my_list = [1, 25, 6, 7, 8]
    # 判断下标是否越界
    if index >= len(my_list):
        print('下标越界：', index)
        # 取值不成功，也需要释放互斥锁，不要影响后面的线程去取值
        # 锁需要在合适的地方进行释放﹐防止死锁

        lock.release()
        return
    # 根据下标取值
    value = my_list[index]
    print(value)
    # 释放锁
    lock.release()


if __name__ == '__main__':
    for i in range(10):
        sub_thread = threading.Thread(target=get_value, args=(i,))
        sub_thread.start()
