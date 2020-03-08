import re
# match()方法
# search()方法  
# 成功则两者都返回的是一个匹配对象，可以用group()方法获取值
# 失败则都返回None
# span()方法返回的是匹配值在原字符串中的位置
s = '83C72DD1D8E93DHF45'
r = re.match('\d',s) #从字符串的第一个字符开始匹配，若不成功则返回空(None)
print(r)
r1 = re.search('\d',s)#搜索整个字符串，找到第一个匹配结果则返回
print(r1.group())
r2 = re.findall('\d',s)
print(r2)