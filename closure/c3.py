# global声明全局变量，必须在函数内部才有效
#非闭包实现
step_num = 0
def go(step):
    global step_num
    new_step = step_num + step
    step_num = new_step
    return new_step
print(go(2))
print(go(3))
print(go(6))