import json
#反序列化
#JSON的数组形式,转换为以列表(List)的形式存储的数据(每个元素以字典的形式表现)
json_str = '[{"name":"zhang", "age":22,"flag":false},{"money":null}]'
# json_str = '{"name":"zhang", "age":22}'#转换为以字典的形式存储的数据
student = json.loads(json_str)
print(type(student))
print(student)