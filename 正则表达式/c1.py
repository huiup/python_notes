import re
a = 'C0C++6C#7Java8Python9Javascipt'
res = re.findall('\D',a)
# re.findall(正则表达式,内容,匹配模式)
print(res)

