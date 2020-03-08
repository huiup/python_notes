""" 
列表推导式
a 可以是集合，字典，元组，列表(即都能推导)
 """
a = {1,2,3,4,5,6,7}
# b可以是集合，字典(c2.py讲解)，列表；元组则会变成一个生成器
b = [i*i for i in a if i > 4]
print(b)
""" 
生成器(generator)可以遍历打印出结果
 """
b = (i*i for i in a if i > 4)
for x in b:
    print(x)