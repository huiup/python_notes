## JSON
+ JSON(JavaScript Object Notation，JavaScript对象标记)是一种轻量级数据**交换格式**  
+ *字符串*是JSON的表现形式  
+ 符合JSON格式的字符串叫做JSON字符串  

### 特点
1. 易于阅读
2. 易于解析
3. 网络传输效率高
4. 跨语言交换数据  

### JSON、JSON对象、JSON字符串  
#### JSON  
没错，它就是一种数据交换的格式
#### JSON对象  
+ 对象可以通过key访问value
+ 例子如下：  
```
json_object = {"name":"zhang", "age":22}#在python中不存在json对象
```
#### JSON字符串  
+ 所谓字符串：单引号''或者双引号""引起来  
+ JSON字符串不能用key访问value
+ 例子如下：
```
json_str = '{"name":"zhang", "age":22}'
```


### JSON数据类型与python对象的转换
#### json库中的loads()方法(反序列化:JSON->python)
*注：json对象中的字符串是用""*

##### 一般JSON格式转换
转换为以字典的形式存储的数据
```python
import json
json_str = '{"name":"zhang", "age":22}'
student = json.loads(json_str)
print(type(student))#<class 'dict'>
print(student)#{'name': 'zhang', 'age': 22}
```
##### JSON的数组形式转换
JSON的数组形式,转换为以列表(List)的形式存储的数据(每个元素以字典的形式表现)
```python
import json
json_str = '[{"name":"zhang", "age":22,"flag":false},{"money":null}]'
student = json.loads(json_str)
print(type(student))#<class 'list'>
print(student)#[{'name': 'zhang', 'age': 22, 'flag': False}, {'money': None}]
```
#### json库中的dumps()方法(序列化:python->JSON)
```python
import json
#序列化 ：字典转换为JSON字符串
student = [
        {"name":"zhang", "age":22,"flag":False},
        {"money":None,"time":"QAQ"}
    ]
json_str = json.dumps(student)
print(type(json_str))#<class 'str'>
print(json_str)#[{"name": "zhang", "age": 22, "flag": false}, {"money": null, "time": "QAQ"}]
```
#### (反)序列化转换总览
|  JSON   | Python  |
|  ----  | ----  |
| object  | dict |
| array  | list |
| string  | str |
| number  | int |
| number  | float |
| true  | True |
| false  | False |
| null  | None |