# map() 会根据提供的函数对指定序列做映射
list_x = [1,2,3,4,5,6,7,8]
def square(x):
    return x * x
r = map(square,list_x)
print(list(r))