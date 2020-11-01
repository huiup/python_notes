#  coding:utf-8
'''
内容:将一个类的接口转换成客户希望的另一个接口。该模式使得原本由于接口不兼容而不能一起工作的那些类可以一起工作。
两种实现方式:
    类适配器:使用多继承
    对象适配器:使用组合
角色:
    目标接口(Target)
    待适配的类 (Adaptee)
    适配器 (Adapter)
适用场景:
    想使用一个已经存在的类，而它的接口不符合你的要求
    (对象适配器)想使用一些已经存在的子类，但不可能对每一个都进行子类化以匹配它们的接口。对象适配器可以适配它的父类接口。


'''
from abc import abstractmethod, ABCMeta


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


class AliPay(Payment):
    def pay(self, money):
        print('支付宝支付%d元' % money)


class BankPay:
    def cost(self, money):
        print('银行卡支付%d元' % money)


class ApplePay:
    def cost(self, money):
        print('苹果支付%d元' % money)

# 对象适配器：组合（在一个类中使用另一个类的方法）
class PaymentAdopter(Payment):
    def __init__(self, payment):
        self.payment = payment

    def pay(self, money):
        self.payment.cost(money)


# 类适配器：多继承
# class NewBankPay(Payment, BankPay):
#     def pay(self, money):
#         self.cost(money)


if __name__ == '__main__':
    # p = NewBankPay()
    # p.pay(100)
    p = PaymentAdopter(ApplePay())
    p.pay(100)
