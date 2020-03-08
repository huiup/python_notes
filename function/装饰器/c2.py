import time
# 使用装饰器
def decorator(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper
def f1():
    print('this is a function')
f = decorator(f1)
f()