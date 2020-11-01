#  coding:utf-8
'''内容:定义一个用于创建对象的接口(工厂接口) ，让子类决定实例化哪一个产品类。
角色:
    抽象工厂角色(PaymentFactory接口)
    具体工厂角色(如：AliPayFactory类)
    抽象产品角色(Payment接口)
    具体产品角色(AliPay类)
优点:
    每个具体产品都对应一个具体工厂类，不需要修改工厂类代码
    隐藏了对象创建的实现细节
缺点︰
    每增加一个具体产品类，就必须增加一个相应的具体工厂类

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


class BankPay(Payment):
    def pay(self, money):
        print('银行卡支付%d元' % money)


class PaymentFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_payment(self):
        pass


class AliPayFactory(PaymentFactory):
    def create_payment(self):
        return AliPay()


class WechatPayFactory(PaymentFactory):
    def create_payment(self):
        return WeChatPay()


class HuabeiFactory(PaymentFactory):
    def create_payment(self):
        return AliPay(True)


class BankFactory(PaymentFactory):
    def create_payment(self):
        return BankPay()


if __name__ == '__main__':
    pf = BankFactory()
    p = pf.create_payment()
    p.pay(100)
