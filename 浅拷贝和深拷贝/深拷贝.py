#  coding:utf-8

import copy

if __name__ == '__main__':
    # 1.不可变类型
    num1 = 1
    num2 = copy.deepcopy(num1)
    print('num1:', id(num1), 'num2:', id(num2))

    str1 = 'hello！'
    str2 = copy.deepcopy(str1)
    print('str1:', id(str1), 'str2:', id(str2))

    tuple1 = (1, 2)
    tuple2 = copy.deepcopy(tuple1)
    print('tuple1:', id(tuple1), 'tuple2:', id(tuple2))

    tuple3 = (1, [3, 4])
    tuple4 = copy.deepcopy(tuple1)
    print('tuple3:', id(tuple3), 'tuple4:', id(tuple4))
    print('tuple3[1]:', id(tuple3[1]), 'tuple4[1]:', id(tuple4[1]))

    # 2.可变类型
    list1 = [1, [2, 3]]
    list2 = copy.deepcopy(list1)
    print('list1:', id(list1), 'list2:', id(list2))
    print('list1[1]:', id(list1[1]), 'list2[1]:', id(list2[1]))

