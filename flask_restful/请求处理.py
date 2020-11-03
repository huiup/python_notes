from flask import Flask
from flask_restful import Resource, Api
from flask_restful.reqparse import RequestParser

# Flask-RESTful提供了RequestParser类，用来帮助我们检验和转换请求数据。
app = Flask(__name__)
api = Api(app)


# /demo?a=1   获取参数a的值
class DemoResource(Resource):
    def get(self):
        # a = request.args.get('a')
        # if not a:
        #     pass
        # else:
        #     pass
        # 用下面代替上面代码
        # 1.创建RequestParser对象
        rp = RequestParser()

        # 2.声明参数
        # rp.add_argument('a')

        # 添加参数检验
        # required:描述请求是否一定要携带对应参数，默认值为False
        # help:参数检验错误时返回的错误描述信息
        # action:描述对于请求参数中出现多个同名参数时的处理方式(?a=1&a=2&a=4)
        #    action='store' 保留出现的第一个，默认
        #    action='append' 以列表追加保存所有同名参数的值
        # type：描述参数应该匹配的类型:普通类型（int,string）、自定义、Flask_RESTful.inputs提供的规则
        # location：描述参数应该在请求数据中出现的位置(form,args,headers,cookies,json,files)
        rp.add_argument('a', required=True, help='missing a param', action='append', type=int)

        # 执行校验
        req = rp.parse_args()
        # 可以将req当做字典或对象操作
        a = req['a']
        # a = req.a

        return {'a': a}


# 使用api对象注册路由
api.add_resource(DemoResource, '/demo')

# 此处启动对于1.0之后的Flask可有可无
# if __name__ == '__main__':
#     app.run()
