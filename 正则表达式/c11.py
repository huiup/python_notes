import re
s = 'life is short,i use python, i love python'
r = re.search('life(.*)python(.*)python',s) #从字符串的第一个字符开始匹配，若不成功则返回空(None)
print(r.group())
print(r.group(0))
print(r.group(1))
print(r.group(2))
print(r.group(0,1,2))
print(r.groups())
# print(r)