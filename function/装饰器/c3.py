import time
# 使用装饰器+语法糖
def decorator(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper
# @ 语法糖
@decorator
def f1():
    print('this is a function')
f1()