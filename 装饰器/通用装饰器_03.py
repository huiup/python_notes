#  coding:utf-8

def decorator(func):
    def inner(*args, **kwargs):
        print('正在执行加法计算！')
        # *args:把元组里面的每一个元素﹐按照位置参数的方式进行传参
        # **kwargs:把字典里面的每一个键值对﹐按照关键字的方式进行传参
        # 这里对字典进行拆包﹐仅限于结合不定长参数的函数使用
        num = func(*args, **kwargs)
        return num

    return inner


@decorator
def add_num(*args, **kwargs):
    # *args：元组类型
    # **kwargs：字典类型
    result = 0
    for value in args:
        result += value
    for value in kwargs.values():
        result += value
    return result


if __name__ == '__main__':
    result = add_num(1,2)
    print(result)
