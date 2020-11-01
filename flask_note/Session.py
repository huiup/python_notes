from flask import Flask, session
# flask将session放到浏览器


app = Flask(__name__)


# 需要先设置SECRET_KEY
class DefaultConfig(object):
    SECRET_KEY = 'afjqiuhqyg8qhgiqeg'


app.config.from_object(DefaultConfig)
# 或者直接设置
# app.secret_key = 'fajfo4t98t'


# 设置session
@app.route('/set_session')
def sett_session():
    session['naget_sessionme'] = 'zhang'
    session['age'] = '22'
    return 'set session ok'


# 读取session
@app.route('/get_session')
def get_session():
    name = session.get('name')
    age = session.get('age')
    return f'get session name : {name},age : {age}'


if __name__ == '__main__':
    app.run()
