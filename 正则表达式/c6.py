import re
# 边界匹配
# ^从字符串的开始匹配
# $从字符串的末尾开始匹配
qq = '100000001'
# 4~8位
r = re.findall('^1000',qq)
print(r)
