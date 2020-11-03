from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
# api:收集类视图和路由信息
api = Api(app)


def decorator1(func):
    def inner(*args, **kwargs):
        print('decorator1')
        return func(*args, **kwargs)

    return inner


def decorator2(func):
    def inner(*args, **kwargs):
        print('decorator2')
        return func(*args, **kwargs)

    return inner


# 1.给类中所有的方法都添加装饰器
class DemoResource1(Resource):
    method_decorators = [decorator1, decorator2]  # 会先打印decorator2

    def get(self):
        return {'msg': 'get view'}

    def post(self):
        return {'msg': 'get view'}


# 2.为类视图中不同的方法添加不同的装饰器
class DemoResource2(Resource):
    method_decorators = {
        'get': [decorator1, decorator2],
        'post': [decorator1]
    }

    # 使用了decorator1 decorator2两个装饰器
    def get(self):
        return {'msg': 'get view'}

    # 使用了decorator1一个装饰器
    def post(self):
        return {'msg': 'get view'}

    # 未使用装饰器
    def put(self):
        return {'msg': 'get view'}


# 注册路由
api.add_resource(DemoResource1, '/demo1')
api.add_resource(DemoResource2, '/demo2')
