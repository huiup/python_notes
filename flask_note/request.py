from flask import Flask
from flask import request
from werkzeug.routing import BaseConverter

app = Flask(__name__)


# 接收的参数：
# string 默认类型
# int
# float
# path   usr/local/src
# uuid
@app.route('/user/<int:user_id>', )
def hello_world(user_id):
    return 'Hello {}'.format(user_id)


# 自定义转换规则
class MobileConverter(BaseConverter):
    regex = r'1[3-9]\d{9}'  # regex固定


app.url_map.converters['mobile'] = MobileConverter


@app.route('/sms_codes/<mobile:mob_num>')
def send_sms_code(mob_num):
    print(type(mob_num))
    return 'send sms code to {}'.format(mob_num)


# 上传图片到服务端
@app.route('/upload', methods=['get', 'POST'])
def upload_file():
    f = request.files['pic']  # f是一个文件对象，上传的文件存放在files中
    # with open('./hui.png', 'wb') as new_file:
    #     new_file.write(f.read())

    # 等价于上面两行
    f.save('./demo.png')
    return 'ok'


if __name__ == '__main__':
    app.run()
