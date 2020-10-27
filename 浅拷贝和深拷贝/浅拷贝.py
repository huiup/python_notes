#  coding:utf-8
import copy

# copy()是一个浅拷贝函数
if __name__ == '__main__':
    # 1.对不可变类型进行浅拷贝实际上是对引用的一个拷贝﹐两个变量指向的是同一个内存地址
    num1 = 1
    num2 = copy.copy(num1)
    print('num1:', id(num1), 'num2:', id(num2))

    tuple1 = (3, 5)
    tuple2 = copy.copy(tuple1)
    print('num1:', id(tuple1), 'num2:', id(tuple2))

    # 2.对可变变量进行拷贝
    list1 = [1, 2, [3, 4]]
    list2 = copy.copy(list1)
    print('list1:', id(list1), 'list2:', id(list2))
    # 对子对象进行操作
    print('list1[2]:', id(list1[2]), 'list2[2]:', id(list2[2]))
