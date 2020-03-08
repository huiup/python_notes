import re
# re.findall(正则表达式,字符内容,匹配模式)
# re.I:不区分大小写
# re.S:对 . 的行为进行改变，使 . 匹配包括换行在内的所有字符
a = 'PythonC#\nJavaPHP'

r = re.findall('c#.{1}', a, re.I | re.S)
print(r)