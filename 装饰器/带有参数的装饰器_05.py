#  coding:utf-8
# 在装饰器外面再包裹上一个函数，让最外面的函数接收参数，返回的是装饰器，因为@符号后面必须是装饰器实例。
def return_decorator(flag):
    # 装饰器，装饰器只能接收一个参数并且是函数类型
    def decorator(func):
        def inner(a, b):
            if flag == "+":
                print("正在努力执行加法计算")
            elif flag == "-":
                print("正在努力执行减法计算")
            func(a, b)

        return inner

    # 当调用函数的时候可以返回一个装饰器decorator
    return decorator


@return_decorator('+')
def add_num(a, b):
    result = a + b
    print(result)


@return_decorator('-')
def sub_num(a, b):
    result = a - b
    print(result)


if __name__ == '__main__':
    add_num(1, 2)
    sub_num(2, 1)
