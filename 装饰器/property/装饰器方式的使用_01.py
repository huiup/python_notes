#  coding:utf-8

#注意:使用装饰器方式的property设置属性那么方法名要保持一致
class Studenet(object):
    def __init__(self):
        self.__age = 0

    @property  # 当对象调用age属性的时候会执行下面的方法
    def age(self):
        print('获取属性！')
        return self.__age

    @age.setter  # 当对象调用age属性设置值的时候会调用下面的方法
    def age(self, new_age):
        print('设置属性！')
        if new_age >= 0 and new_age < 110:
            self.__age = new_age
        else:
            print('设置年龄不正确')


if __name__ == '__main__':
    s = Studenet()
    print(s.age)
    s.age = 100
    print(s.age)
