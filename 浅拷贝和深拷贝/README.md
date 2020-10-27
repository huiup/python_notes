### 浅拷贝和深拷贝

##### 1.浅拷贝

`copy()`函数是浅拷贝，只对**可变类型**的第一层对象进行拷贝，对拷贝的对象开辟**新的内存空间**进行存储，**不会拷贝对象内部的子对象**。

- 不可变类型：数字、字符串、元组

  注：对不可变类型进行浅拷贝实际上是对**引用**的一个拷贝，两个变量指向的是同一个内存地址

```python
import copy
# copy()是一个浅拷贝函数
num1 = 1
num2 = copy.copy(num1)
print('num1:', id(num1), 'num2:', id(num2))
# 内存地址相同

tuple1 = (3, 5)
tuple2 = copy.copy(tuple1)
print('num1:', id(tuple1), 'num2:', id(tuple2))
# 内存地址相同
```

- 可变类型：列表、字典、集合

```python
import copy
# copy()是一个浅拷贝函数
list1 = [1, 2, [3, 4]]
list2 = copy.copy(list1)
print('list1:', id(list1), 'list2:', id(list2))
# 内存地址不同

#查看子对象
print('list1[2]:', id(list1[2]), 'list2[2]:', id(list2[2]))
# 内存地址相同
```

##### 2.深拷贝

`deepcopy()`函数是深拷贝。只要发现对象**有可变类型**那么就对该对象直到最后一个可变类型的**每一层对象进行拷贝**，拷贝成功后会开辟新的内存空间

- 不可变类型：数字、字符串、**元组**

```python
import copy
num1 = 1
num2 = copy.deepcopy(num1)
print('num1:', id(num1), 'num2:', id(num2))
# 内存地址相同

str1 = 'hello！'
str2 = copy.deepcopy(str1)
print('str1:', id(str1), 'str2:', id(str2))
# 内存地址相同

tuple1 = (1, 2)
tuple2 = copy.deepcopy(tuple1)
print('tuple1:', id(tuple1), 'tuple2:', id(tuple2))
# 内存地址相同

# 当元组里有可变类型时，会对元组和子元素列表进行拷贝，拷贝后都会产生一个新的内存空间
tuple3 = (1, [3, 4])
tuple4 = copy.deepcopy(tuple1)
print('tuple3:', id(tuple3), 'tuple4:', id(tuple4))
# 内存地址不相同
print('tuple3[1]:', id(tuple3[1]), 'tuple4[1]:', id(tuple4[1]))
# 内存地址不相同
# tuple3[1][1]和tuple4[1][1]的内存地址也不同，但tuple3[0]和tuple4[0]的地址相同
```

- 可变类型：列表、字典、集合

  可变类型对应深拷贝来说也会进行拷贝，如果发现子对象也是可变类型也会进行拷贝，拷贝后会开辟新的内存空间存储拷贝后的对象

```python
import copy
list1 = [1, [2, 3]]
list2 = copy.deepcopy(list1)
print('list1:', id(list1), 'list2:', id(list2))
# 内存地址不相同
print('list1[1]:', id(list1[1]), 'list2[1]:', id(list2[1]))
# 内存地址不相同
```

##### 3.两者的区别

- 浅拷贝最多拷贝对象的一层
- 深拷贝可能拷贝对象的多层