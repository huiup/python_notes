#  coding:utf-8

'''
内容:保证一个类只有一个实例，并提供一个访问它的全局访问点。
角色:
    单例(Singleton)
优点︰
    对唯一实例的受控访问
    单例相当于全局变量，但防止了命名空间被污染

'''


class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            # cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance = object.__new__(cls)
        return cls._instance


class MyClass(Singleton):
    def __init__(self, a):
        self.a = a


if __name__ == '__main__':
    a = MyClass(10)
    b = MyClass(20)
    print(a.a)
    print(b.a)
    print(id(a), id(b))  # 同一实例
