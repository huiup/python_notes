from flask import Flask
import json

# 配置对象方式加载配置信息
class DefaultConfig():
    '''
    默认配置
    '''
    SECRET_KEY = 'sdadg345dfg42dagd3245'


class DEBUGConfig(DefaultConfig):
    DEBUG = True


# 工厂函数
def CreateFlaskApp(config):
    app = Flask(__name__)
    # 配置对象
    app.config.from_object(config)
    return app


app = CreateFlaskApp(DEBUGConfig)


# 通过py文件设置配置信息
# app.config.from_pyfile('setting.py')

# @app.route('/')
# def hello_world():
#     return 'Hello World!'

# 读取配置信息
# print(app.config['SECRET_KEY'])
# print(app.config['DEBUG'])

# 查看路由信息（终端：flask routes）
# print(app.url_map)
# 遍历url_map
# for rule in app.url_map.iter_rules():
#     print(f'name = {rule.endpoint} path = {rule.rule}')

# 遍历url_map，取出特定信息，在一个特定的接口返回
@app.route('/')
def route_map():
    rules_iterator = app.url_map.iter_rules()
    return json.dumps({rule.endpoint: rule.rule for rule in rules_iterator})



if __name__ == '__main__':
    app.run()
