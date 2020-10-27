#  coding:utf-8
# 在函数里面看到有yield关键字﹐那么这个函数就是生成器

def my_generator():
    for i in range(5):
        print('开始生成数据...')
        # 当程序执行到yield关键字的时候代码暂停并把结果返回﹐再次启动生成器的时候会在暂停的位置继续往下执行
        yield i
        print('上一次数据生成完毕!')


if __name__ == '__main__':
    result = my_generator()  # 要先调用

    # 1.普通取值
    # print(next(result))

    # 2.常用取值
    for value in result:
        print(value)