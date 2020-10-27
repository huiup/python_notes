#  coding:utf-8

my_generator = (i * 2 for i in range(5))

if __name__ == '__main__':
    # 遍历时，当生成器已经没有值时，会抛出StopIteration，表示生成器生成数据完毕
    # 1.第一种取值
    # value = next(my_generator)
    # print(value)

    # 2.第二种取值
    # while True:
    #     try:
    #         value = next(my_generator)
    #         print(value)
    #     except Exception as e:
    #         break

    # 3.第三种取值（常用）
    # for循环内部循环调用next函数获取生成器中的下一值，当出现异常for循环内部自动进行了异常捕获
    for value in my_generator:
        print(value)
