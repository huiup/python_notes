def f1():
    a = 10
    def f2():
        # a = 20#此a被python认为是一个局部变量
        # print(a)
        c = a * 10
    # print(a)
    return f2
    # print(a)
f = f1()
print(f)
print(f.__closure__)