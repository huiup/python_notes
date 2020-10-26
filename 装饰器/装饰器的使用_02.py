#  coding:utf-8
import time


# 定义装饰器
def decorator(func):
    def inner():
        # 内部函数对已有函数进行装饰
        # 获取时间
        begin = time.time()
        func()
        end = time.time()
        print('函数执行完成耗时：', end - begin)

    return inner


@decorator
def work():
    for i in range(10000):
        print(i)


if __name__ == '__main__':
    work()

