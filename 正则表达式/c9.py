import re
# sub()方法，替换
# a = 'PythonC#JavaPHPC#C#C#'
# b = a.replace('C#','GO')
s = 'A8C3721D86'
def convert(value):
    matched = value.group()#得到具体的字符
    if int(matched) >= 6:
        return '9'
    else:
        return '0'
r = re.sub('\d',convert,s)
print(r)