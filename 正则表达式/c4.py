import re
# 数量词
# * 匹配前一个字符0次或无限多次
# + 匹配一次或无限多次
# ? 匹配0次或1次
# a = 'python 1111 Java678php'
a = 'pytho0python1pythonn2'

r = re.findall('python{1,2}',a)
print(r)
