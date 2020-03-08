# lambda 与 map
# 单个参数
# list_x = [1,2,3,4,5,6,7,8]
# r = map(lambda x: x*x,list_x)
# print(list(r))
# 多个参数
list_x = [1,2,3,4,5,6,7,8]
list_y = [1,2,3,4,5,6]
r = map(lambda x, y: x*x + y,list_x, list_y)
print(list(r))
#注:①lambda引号前的参数个数须与map的第二个可变参数个数保持一致*  
#注:②本例中输出列表中元素的个数取决于参数列表长度较少的那个*