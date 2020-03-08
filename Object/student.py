# import people
from people import Human
class Student(Human):#继承
    # sum = 0
    def __init__(self,school,name,age):
    #     #构造函数
    #     #初始化对象的属性
        self.school = school
        super(Student,self).__init__(name,age)#调用父类的方法
        # Human.__init__(self,name,age)
    def do_homework(self):
        super(Student,self).do_homework()
        print('homework')#同名时，调用的是子类的方法

student1 = Student('清水小学','zhang',18)
student1.do_homework()
# print(student1.sum)
# print(Student.sum)
# print(student1.name)
# print(student1.age)
# student1.get_name()