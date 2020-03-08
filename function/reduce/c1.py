from functools import reduce
# 需要导入reduce
# 连续计算，连续调用lambda，直到序列遍历完
# reduce()是返回一个值
list_x = [1,2,3,4,5,6,7,8]
r = reduce(lambda x, y: x + y,list_x)
print(r)
# 运行顺序为(((1+2)+3)+4)+5...