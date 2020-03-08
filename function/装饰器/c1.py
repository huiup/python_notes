import time
# 不使用装饰器时
# 开闭原则：对修改是封闭的，对扩展是开放的
# 新加业务逻辑：添加运行函数时打印运行时间的功能
# 允许向一个现有的对象添加新的功能，同时又不改变其结构。
def print_time(func):
    print(time.time())
    func()
def f1():
    print('this is a function')

print_time(f1)

