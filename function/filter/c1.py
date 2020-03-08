""" 
list_x = [1,0,1,0,1,1,1,0]
r = filter(lambda x: True if x==1 else False, list_x)
print(list(r))
函数返回的是一个布尔值，表示当前元素是否应该存在于列表中
 """
list_x = [1,0,1,0,1,1,1,0]
r = filter(lambda x: x, list_x)
print(list(r))