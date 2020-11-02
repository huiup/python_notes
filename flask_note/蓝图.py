from flask import Flask, Blueprint

app = Flask(__name__)
# 创建蓝图对象
user_bp = Blueprint('user', __name__)


@user_bp.route('/profile')
def get_profile():
    return 'user profile'


# 注册蓝图
app.register_blueprint(user_bp)
# 添加前缀：/user/profile
# app.register_blueprint(user_bp, url_prefix='/user')

# 其他方式
from goods_BP import goods

app.register_blueprint(goods)

if __name__ == '__main__':
    app.run(debug=True)
