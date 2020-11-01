#  coding:utf-8
'''
意图：定义一个用于创建对象的接口,让子类决定实例化哪一个类。
内容:不直接向客户端暴露对象创建的实现细节，而是通过一个工厂类来负责创建产品类的实例。
角色：
    工厂角色(PaymentFactory类)：根据参数输出具体产品
    抽象产品角色(Payment接口)：定义产品的必要功能。
    具体产品角色(WeChatPay，AliPay类)：具体实例化出来的对象。
优点︰
    隐藏了对象创建的实现细节
    客户端不需要修改代码
缺点︰
    违反了单一职责原则，将创建逻辑集中到一个工厂类里，当添加新产品时，需要修改工厂类代码，违反了开闭原则
'''

from abc import abstractmethod, ABCMeta


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


class AliPay(Payment):
    def __init__(self, use_huabei=False):
        self.use_huabei = use_huabei

    def pay(self, money):
        if self.use_huabei:
            print('花呗支付%d元' % money)
        else:
            print('支付宝余额支付%d元' % money)


class WeChatPay(Payment):
    def pay(self, money):
        print('微信支付%d元' % money)


class PaymentFactory():
    def create_payment(self, method):
        if method == 'huabei':
            return AliPay(use_huabei=True)
        elif method == 'alipay':
            return AliPay(False)
        elif method == 'Wechat':
            return WeChatPay()


if __name__ == '__main__':
    pf = PaymentFactory()
    p = pf.create_payment('huabei')
    p.pay(100)
