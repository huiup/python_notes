import re
# 组 用括号把一系列字符括起来，则叫做组

a = 'PythonPythonPythonPython'

r = re.findall('(Python){3}',a)
print(r)