import time
# 使用装饰器+语法糖(带参数)
def decorator(func):
    def wrapper(func_name):
        print(time.time())
        func(func_name)
    return wrapper
@decorator
def f1(func_name):
    print('this is a function named ' + func_name)
f1('f1')