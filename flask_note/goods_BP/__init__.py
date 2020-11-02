#  coding:utf-8
from flask import Blueprint

goods = Blueprint('goods', __name__)
# 导入视图文件，否则views文件不会载入
# 为什么放在下面：因为放上面会无法导入（模块循环导入）
from . import views
