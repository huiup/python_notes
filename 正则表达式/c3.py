import re
# 概况字符集
a = 'Pytho\nn 1\t111 Ja\rva678&php'
r = re.findall('\s',a)
# \d数字 \D非数字
# \w匹配单词字符，等价于[A-Za-z0-9_] \相反
# \s空白字符 \n \t \r 空格     \S相反
# . 匹配除换行符(\n)之外其他所有字符
print(r)

