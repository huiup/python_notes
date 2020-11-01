from flask import Flask, request, abort

app = Flask(__name__)
'''
异常主动抛出:
abort()方法
    抛出一个给定状态代码的HTTPException或者指定响应，例如想要用一个页面未找到异常来终止
请求，你可以调用abort(404)。
    参数︰code - HTTP的错误状态码
'''


# 正确传参：/book?book_id=123
# 错误传参：/book
@app.route('/book')
def book():
    book_id = request.args.get('book_id')
    if  book_id is None:
        abort(400)  # 400 Bad Request
    return f'book_id is {book_id}'


'''
捕获错误：
errorhandler装饰器：
    注册一个错误处理程序，当程序抛出指定错误状态码的时候，就会调用该装饰器所装饰的方法
参数:
    HTTP的错误状态码或指定异常

'''
# 例如统一处理状态码为404的错误给用户友好的提示:
@app.errorhandler(404)
def server_error(e):  # 此处有个参数e，异常类的具体对象
    return '没有找到哟！'

# 例如统一处理状态码为500的错误给用户友好的提示:
@app.errorhandler(500)
def server_error(e):  # 此处有个参数e，异常类的具体对象
    return '服务器错误！'

# 捕获指定异常，当视图函数中出现指定错误，则会调用
@app.errorhandler(ZeroDivisionError)
def zero_division_error(e):  # 此处有个参数e，异常类的具体对象
    print(e)
    return '除数不能为0'


@app.route('/test')
def test():
    a = 1 / 0
    return '1/0'


if __name__ == '__main__':
    app.run()
