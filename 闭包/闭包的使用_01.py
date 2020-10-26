#  coding:utf-8
# 外部函数接收姓名参数


def config_name(name):
    # 内部函数保存外部函数的参数﹐并且完成数据显示的组成
    def inner(msg):
        print(name + ':' + msg)

    # 外部函数要返回内部函数
    return inner


if __name__ == '__main__':
    # 创建tom 闭包实例（对象)
    tom = config_name("tom")
    # 创建jerry 闭包实例
    jerry = config_name("jerry")
    # 如果执行tom闭包，因为已经保存了name参数，那么以后在输入的时候都是, tom说:xxx
    tom('jerry！ 过来玩儿啊！')
    jerry('打死都不去!')
    tom('我不吃你')
    jerry('你个糟老头子，坏的很！')
