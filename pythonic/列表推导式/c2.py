# 字典的推导式
students = {
    '张三' : 18,
    '李四' : 20,
    '王五' : 22
}
# 字典得用items()方法 
# 获取key:value,大括号{}(字典)
b = {key:value for key,value in students.items()}
print(b)#{'张三': 18, '李四': 20, '王五': 22}
# 颠倒为value：key
b = {value:key for key,value in students.items()}
print(b)#{18: '张三', 20: '李四', 22: '王五'}
# 获取value
b = {y for x,y in students.items()}
print(b)#{18, 20, 22}
# 获取一对
b = {x for x in students.items()}
print(b)#{('张三', 18), ('李四', 20), ('王五', 22)}