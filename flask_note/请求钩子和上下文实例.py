from flask import Flask, abort, g

app = Flask(__name__)


# 请求钩子（尝试判断用户的身份，对于未登录用户不做处理，放行)用g对象保存用户身份信息
@app.before_request
def authentication():  # 身份验证
    # 利用before_request请求钩子，在进入所有视图前先尝试判断用户身份
    # TODO 此处利用鉴权机制（如cookie、session、jwt等）鉴别用户身份信息
    # if已登录用户，用户有身份信息
    g.user_id = 123
    # else未登录用户,用户无身份信息
    # g.user_id = None


# 强制登录装饰器
def decorator(func):
    def inner(*args, **kwargs):
        # 判断用户是否登录
        if g.user_id is None:
            abort(401)  # 401：表示请求需要认证
        else:
            # 已登录
            return func(*args, **kwargs)
    return inner


# 普通视图，不需要验证
@app.route('/')
def index():
    return f'欢迎来到主页！您的user_id为:{g.user_id}'


# 需要验证
@app.route('/user')
@decorator
def get_user_id():
    return f'您的user_id为：{g.user_id}'



if __name__ == '__main__':
    app.run()
