step_num = 0
def go(pos):
    def go1(step):
        nonlocal pos#声明不是局部变量
        new_pos = pos + step
        pos = new_pos
        return new_pos
    return go1

p = go(step_num)
print(p(2))
print(p.__closure__[0].cell_contents)
print(p(3))
print(p.__closure__[0].cell_contents)
print(p(6))
print(p.__closure__[0].cell_contents)