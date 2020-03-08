import time
# 使用装饰器+语法糖(带不同个数的参数)
# *args 可变参数
def decorator(func):
    def wrapper(*args):
        print(time.time())
        func(*args)
    return wrapper
@decorator
def f1(func_name):
    print('this is a function named ' + func_name)
@decorator
def f2(func_name1, func_name2):
    print('this is a function named ' + func_name1)
    print('this is a function named ' + func_name2)
f1('test func')
f2('test func1','test func2')