#  coding:utf-8

class Studenet(object):
    def __init__(self):
        self.__age = 0

    def get_age(self):
        print('获取属性！')
        return self.__age

    def set_age(self, new_age):
        print('设置属性！')
        if new_age >= 0 and new_age < 110:
            self.__age = new_age
        else:
            print('设置年龄不正确')

    # 1. get_age表示获取age属性的时候执行的方法
    # 2. set_age表示设置age属性的时候执行的方法
    age = property(get_age, set_age)


if __name__ == '__main__':
    s = Studenet()
    print(s.age)
    s.age = 100
    print(s.age)
