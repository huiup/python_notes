from flask import Flask, render_template, redirect, jsonify, make_response

app = Flask(__name__)


# 返回模板
@app.route('/index')
def index():
    my_list = ['1', '2', '3']
    my_str = '123'
    my_dict = dict(
        my_list=['1', '2', '3'],
        my_str='123'
    )
    return render_template('index.html', my_list=my_list, my_str=my_str)
    # 以下两种方式等价
    # return render_template('index.html', **my_dict)
    # return render_template('index.html', my_list=['1', '2', '3'], my_str='123')


# 重定向
@app.route('/redirect')
def change():  # 注：视图函数名不能为redirect
    return redirect('https://www.baidu.com/')


# 返回json数据
@app.route('/json')
def demo3():
    json_dict = {
        "user_id": 10,
        "user_name": 'zhang'
    }
    return jsonify(json_dict)


@app.route('/status')
def demo4():
    # return '状态码为 666'  # (response)
    # return '状态码为 666', 666  # (response, status)
    # return '状态码为 666', 666, [('Name', 'Zhang')]  # (response, status, headers)
    return '状态码为 666', 666, {'Name': 'Zhang'}  # (response, status, headers)


@app.route('/demo5')
def demo5():
    resp = make_response('make response测试')
    resp.headers["Name"] = 'Zhang'
    resp.status = "404 not found"
    return resp

if __name__ == '__main__':
    app.run()
