#  coding:utf-8
# 类装饰器：使用类装饰已有函数

class MyDecorator(object):
    def __init__(self, func):
        self.__func = func

    # 实现__call_这个方法﹐让对象变成可调用的对象
    def __call__(self, *args, **kwargs):
        # 对已有函数进行封装
        print('嘟！嘟！嘟！')
        self.__func()



@MyDecorator
def show():
    print('咚！咚！咚！')


if __name__ == '__main__':
    # 执行show，相当于执行MyDecorator类创建实例对象-->show()-->对象()
    show()
