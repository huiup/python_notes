import re
# 贪婪 与 非贪婪
# 默认贪婪 ? 前为一个区间
a = 'python 1111 Java678php'
r = re.findall('[a-z]{3,6}?',a)
print(r)