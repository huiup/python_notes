#  coding:utf-8

def fibonacci(num):
    # 初始化前两个值
    a = 0
    b = 1
    # 记录每次生成个数的索引
    current_index = 0
    while current_index < num:
        result = a
        # 条件成立，交换两个变量的值
        a, b = b, a + b
        current_index += 1
        yield result


if __name__ == '__main__':
    f = fibonacci(50)
    for value in f:
        print(value)
