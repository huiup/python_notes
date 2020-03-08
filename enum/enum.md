## python中的枚举  
+ 在pytho中使用枚举需要继承enum类(from enum import Enum)

### 枚举相比普通类和字典的优点
|枚举|字典|普通类|
|:---|----|----|
| class VIP(Enum):<br>YELLOW = 1<br>GREEN = 1 | a = {'yellow':1,'green':2} |  class test():<br>Yellow = 1<br>Green = 1   |
+ 防止值可变的功能
+ 防止相同标签的功能  
### 枚举的一般使用  
+ 获取枚举的类型
+ 获取枚举的名称
+ 获取枚举的值
```python
from enum import Enum
class VIP(Enum):
    YELLOW = 1
    GREEN = 1
print(VIP.YELLOW)#VIP.YELLOW
print(type(VIP.YELLOW))#<enum 'VIP'>
#获取枚举的名称
print(VIP.YELLOW.name)#YELLOW
print(type(VIP.YELLOW.name))#<class 'str'>
#获取枚举的值
print(VIP.YELLOW.value)#1
print(type(VIP.YELLOW.value))#<class 'int'>
# 获取名称所对应的枚举类型
print(VIP['GREEN'])#VIP.YELLOW
print(type(VIP['GREEN']))#<enum 'VIP'>
```
### 枚举的遍历
```python
from enum import Enum
class TEST(Enum):
    YELLOW = 1
    GREEN = 2
    RED = 4
for v in VIP:
    print(v)
print(len(TEST))#3
#遍历结果如下：
# VIP.YELLOW
# VIP.GREEN
# VIP.RED
```  
**注意事项:当枚举中有值相同的两个(多个)名称时，其他的都将作为是第一个的别名**  

```python
from enum import Enum
class TEST2(Enum):
    YELLOW = 1#此处有两个1
    GREEN = 1
    RED = 4
for v in TEST2:
    print(v)
print(len(TEST2))#2
#遍历结果如下：
# VIP2.YELLOW
# VIP2.RED
```  
+ 怎样将别名也打印出来  
```python
class TEST2(Enum):
    YELLOW = 1
    GREEN = 1
    RED = 4
for v in TEST2.__members__:
    print(v)
# 输出结果为：
# YELLOW
# GREEN
# RED
```
### 枚举之间的比较（python中）
+ 枚举之间可以做等值比较
+ 枚举之间不能做大小比较
+ 可以做身份比较

```python
from enum import Enum
# 枚举之间的比较
class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    RED = 4
class VIP1(Enum):
    YELLOW = 1
    GREEN = 2
    RED = 4
# result = VIP.GREEN > VIP.GREEN 会报错
result = VIP.GREEN == VIP.GREEN
print(result)#True
result = VIP.GREEN == VIP1.GREEN
print(result)#False
result = VIP.GREEN is VIP.GREEN
print(result)#True
```  
### 枚举的转换  
+ 通过值获取枚举
```python
from enum import Enum
class VIP(Enum):
    YELLOW = 1
    GREEN = 2
    RED = 4
a = 1
print(VIP(a))# VIP.YELLOW
print(VIP(a).name)# YELLOW
```  
### 枚举拓展
#### IntEnum(取整)
```python
from enum import IntEnum
class VIP(IntEnum):
    YELLOW = 1
    TEST = 1.9#取整为1，此时TEST为YELLOW的别名
    GREEN = 2
    # BLUE = 'str'#值中不能出现字符，会报错！！
    GRAY = '3'#数字字符将会自动转换为数字
    # TEST2 = '3.0'#引号中得是整数，会报错！！！
    RED = 4
```  
#### unique(唯一)
```python
from enum import Enum,unique
@unique
class VIP(Enum):
    YELLOW = 1
    TEST = 1#引入@unique后，枚举类型不能取相同的value，也不能成为别名，会报错！！
    # TEST = 5#枚举类中的key也不能相同
    GREEN = 2
    RED = 4
```  
