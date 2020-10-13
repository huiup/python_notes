#面向对象

class Student():
    sum = 1
    # name = 'eryue'
    # age = 0
    def __init__(self,name,age):
        #构造函数
        #初始化对象的属性
        self.name = name
        self.age = age
        self.__score = 1#私有
        self.__class__.sum += 1
        # print(name)# 此name 是形参的name
        # print(self.name)
        # print('name :'+name+'   age :'+str(age))
        # print(self.__class__.age)访问类变量
    def marking(self,score):
        if score < 0:
            score = 0
            # return '不能为负数！'
        self.__score = score
        print(self.name + '分数为：' + str(self.__score))
    def do_homework(self):
        self.do_english_homework() 
        print('homework')

    def do_english_homework(self):
        print('english_homework')

    @classmethod#类方法，用来操作类变量
    def plus_sum(cls):#cls代表当前类
        cls.sum += 1#不能访问实例变量
        print(cls.sum)
    @staticmethod#静态方法，可以被类和对象调用，也可以访问类变量
    def add(x,y):#不能访问实例变量
        print(Student.sum)
        print('this is static method')
        


class Printer():
    def print_file(self):
        print('name: '+self.name)
        print('age: '+str(self.age))
    
student1 = Student('zhang',23)
# student2 = Student('mou',18)
# res = student1.marking(59)
# student1.__score = -1 #相当于给student1添加了一个新的__score 属性，所以能够修改和访问
print(student1.__dict__)
# print(student2._Student__score)





