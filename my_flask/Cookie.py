from flask import Flask, make_response, request

app = Flask(__name__)


# 设置cookie
@app.route('/cookie')
def cookie():
    resp = make_response('set cookie ok')
    resp.set_cookie('name', 'zhang', max_age=3600)  # 设置cookie有效期
    return resp


# 读取cookie
@app.route('/get_cookie')
def get_cookie():
    resp = request.cookies.get('name')
    return resp


# 删除cookie（删除方式为：设置set_cookie中的创建日期为1970年且max_age=0）
@app.route('/delete_cookie')
def delete_cookie():
    resp = make_response('delete cookie ok')
    resp.delete_cookie('name')
    return resp


if __name__ == '__main__':
    app.run()
