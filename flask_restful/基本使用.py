from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
# api:收集类视图和路由信息
api = Api(app)


# 类视图
# 继承Resource
class HelloWorldResource(Resource):
    def get(self):
        # restful中，可以直接返回字典，会自动转换成json
        return {'hello': 'world '}

    def post(self):
        return {'msg ': 'post hello world '}


# 使用api对象注册路由
api.add_resource(HelloWorldResource, '/')

# 此处启动对于1.0之后的Flask可有可无
# if __name__ == '__main__':
#     app.run()
