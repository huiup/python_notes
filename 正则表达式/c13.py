import json
#序列化 ：字典转换为JSON字符串
student = [
        {"name":"zhang", "age":22,"flag":False},
        {"money":None,"time":"QAQ"}
    ]
json_str = json.dumps(student)
print(type(json_str))
print(json_str)