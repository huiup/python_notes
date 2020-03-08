# 闭包:函数+环境变量（函数定义时候）
#功能，能够保留（记住）函数上一次调用的状态
def curve_pre():
    a = 25
    def curve(x):
        # print('this is a function')
        # return ax^2 + bx + c
        return a*x*x
    return curve
a = 10
f = curve_pre()#环境变量a被放到__closure__中，随着curve一起返回
print(f.__closure__)
print(f.__closure__[0].cell_contents)
print(f(2))