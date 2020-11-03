from flask_restful import Resource, fields, marshal_with, marshal, Api
from flask import Flask

# Flask-RESTful提供了marshal工具，用来帮助我们将数据序列化为特定格式的字典数据,以便作为视图的返回值。


app = Flask(__name__)
api = Api(app)


class User:
    def __init__(self, user_id, name, age):
        self.user_id = user_id
        self.name = name
        self.age = age


# 声明需要序列化处理的字段:只返回user_id和name字段
resource_fields = {
    'user_id': fields.Integer,
    'name': fields.String
}


# 使用装饰器的方式
class Demo1(Resource):
    @marshal_with(resource_fields, envelope='data1')  # envelope再内嵌一个字典
    def get(self, ):
        user = User(1, 'Jack', 22)
        return user


# 函数方式
class Demo2(Resource):
    def get(self):
        user = User(1, 'Jack', 22)
        return marshal(user, resource_fields, envelope='data1')


api.add_resource(Demo2, '/')
