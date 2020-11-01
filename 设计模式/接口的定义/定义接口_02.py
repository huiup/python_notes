#  coding:utf-8
from abc import abstractmethod, ABCMeta


# 接口：若干抽象方法的集合。
# 当接口有多个抽象方法时，子类必须实现接口中的全部方法才不报错
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


class AliPay(Payment):
    def pay(self, money):
        print('支付宝支付%d元' % money)


class WeChatPay(Payment):
    pass


if __name__ == '__main__':
    p1 = AliPay()
    # p2 = WeChatPay()
    # 当子类未实现接口的pay方法时，调用pay时会报错；若不调用pay方法，也会报错
    p1.pay(100)
    # 继承接口的类未实现pay方法，则会报错
    # p2.pay(100)
