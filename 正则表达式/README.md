正则表达式是一个特殊的字符序列(普通字符、元字符)，一个字符串是否与我们所设定的字符序列相匹配。

## 表达式简单介绍

### 字符集：
+ `a[a-z]c  [A-Za-z0-9_]`
+  []表示：里面的字符为'或'关系
+ ()组 表示：里面的字符为'且'关系
+ |表示：匹配左右任意一个表达式
+ -表示：从左到右这一区间
+ ^表示：非关系 如：`[^0-9]`：0-9都不匹配

### 概况字符集：
+ `\d`数字     \D非数字
+ `\w`匹配字符，等价于`[A-Za-z0-9_]`和汉字       \W相反
+ `\s`空白字符 \n \t \r 空格          \S相反
+ `.` 匹配除换行符(\n)之外其他所有字符 （`\.`表示对正则表达式里面的.进行了转义,变成了一个普通的点，只能匹配.字符）
+ `\num` ：引用分组匹配到的数据.如：`re.match("<([a-zA-Z1-6]+)>.*</\\1>","<html>hh</html>")`，使前后标签匹配的内容保持一致
+ `(?P<name>) (?P=name)`：给分组起别名和引用分组匹配到的字符(P大写)。如：`re.match("<(?P<name1>[a-zA-Z1-6]+)>.*</(?P=name1)>","<html>hh</html>")`

### 数量词：(匹配的是字符或表达式)
+ 如：`[a-z]{3,6}`
+ *表示：匹配0次或无限多次
+ +表示：匹配一次或无限多次
+ ?表示 匹配0次或1次
+ {}表示：匹配的次数
+ {3,6}表示：匹配3到6次

### 贪婪与非贪婪(python默认为贪婪)：
+ 非贪婪的表示：[a-z]{3,6}? (注：当?前面的子表达式是一个范围时，则表示为非贪婪)

### 边界匹配：
+ ^表示：匹配开头
+ $表示：匹配末尾

## python中re模块中几个常用的方法
### sub()方法：(替换)
sub(正则表达式,替换内容,原字符内容[,替换次数,匹配规则])
```sub(pattern, repl, string[, count=0, flags=0])```
string也可以为一个函数
count:默认为0，表示替换不限制次数；为1则替换1次

```python
import re
s = 'A8C3721D86'
def convert(value):
    matched = value.group()#得到具体的字符
    if int(matched) >= 6:
        return '9'
    else:
        return '0'
r = re.sub('\d',convert,s)
print(r)# A9C0900D99
```
### findall()方法：(查找)
`findall(pattern, string[, flags=0])`
findall(正则表达式,字符内容[,匹配模式])
可选参数'匹配模式'的介绍：
re.I：让匹配不区分大小写
re.S：对.行为进行改变，使.匹配包括换行(\n)在内的所有字符。  
多的模式用'|'间隔，如：findall(正则表达式,字符内容[re.I | re.S])  

### match()方法
`match(pattern, string, flags=0)`
功能：从字符串的第一个字符开始匹配，若不成功则返回空(None)，匹配成功就返回。成功就返回一个包含匹配信息的对象，用group()方法获取值，span()方法获取匹配值在原字符串中的位置。  

### search()方法
`search(pattern, string, flags=0)`
功能：搜索整个字符串，找到第一个匹配结果就返回(我也溜了)，不成功就返回None。返回一个包含匹配信息的对象，可以用group()方法获取值,span()方法获取匹配值在原字符串中的位置。  

### group()方法代码详解:  
功能：用来提取分组截获的字符串，一个()代表一个分组
参数讲解：
group()与group(0)等价，都返回完整的内容
group(1)获取第1个分组的内容
group(2)获取第2个分组的内容
group(0,1,2)返回它们获取的内容，统一装入一个元组中
groups()返回所有分组匹配的字符，以元组的格式

```python
import re
s = 'life is short,i use python, i love python'
r = re.search('life(.*)python(.*)python',s)
print(r.group())#life is short,i use python, i love python
print(r.group(0))#life is short,i use python, i love python
print(r.group(1))# is short,i use
print(r.group(2))#, i love
print(r.groups())#(' is short,i use ', ', i love ')
```
