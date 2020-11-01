#  coding:utf-8


# 接口：若干抽象方法的集合。
# 作用:限制实现接口的类必须按照接口给定的调用方式实现这些方法;对高层模块隐藏了类的内部实现。


class Payment():
    # 抽象方法的集合，继承该类的子类必须实现该方法
    def pay(self, money):
        raise NotImplementedError


# 此处继承Payment类，但不实现pay方法
class AliPay(Payment):
    pass


class WeChatPay(Payment):
    def pay(self, money):
        print('支付宝支付%d元' % money)


if __name__ == '__main__':
    p1 = AliPay()
    p2 = WeChatPay()
    # 问题：当子类未实现接口的pay方法时，调用pay方法则会报错；若不调用pay方法，则不会报错
    # p1.pay(100)
    p2.pay(100)
