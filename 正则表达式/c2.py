import re
# 字符集 
a = 'abc, acc, adc, aec, afc, ahc'
r = re.findall('a[c-f]c',a)
print(r)