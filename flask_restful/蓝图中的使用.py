from flask import Flask, Blueprint
from flask_restful import Resource, Api

app = Flask(__name__)
user_bp = Blueprint('user', __name__)
api = Api(user_bp)


# 类视图
class UserInfoResource(Resource):
    def get(self):
        # restful中，可以直接返回字典，会自动转换成json
        return {'name': 'Jack', 'age': 22}


# 使用api对象注册路由
api.add_resource(UserInfoResource, '/user/info')

app.register_blueprint(user_bp)
