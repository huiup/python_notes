#  coding:utf-8

from . import goods


@goods.route('/goods')
def get_goods():
    return 'user goods'
