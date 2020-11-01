#  coding:utf-8
from contextlib import contextmanager


# 加上装饰器这个代码﹐那么下面函数创建的对象就是一个上下文管理器
@contextmanager
def file_open(file_name, file_mode):
    try:
        file = open(file_name, file_mode)
        # yield关键字之前的代码可以认为是上文方法﹐负责返回操作对象资源
        yield file
    except Exception as e:
        print(e)
    finally:
        # yield关键字后面的代码可以认为是下文方法﹐负责释放操作对象的资源
        print('over')
        file.close()


if __name__ == '__main__':
    with file_open('1.txt', 'r') as file:
        data = file.write()
        print(data)
