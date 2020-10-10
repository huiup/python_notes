#  coding:utf-8

import threading


def show_info(name, age):
    # print(f'name:{name} age:{age}')
    print('name:{} age:{}'.format(name, age))


if __name__ == '__main__':
    # 以元组方式传参﹐要保证元组里面元素的顺序和函数的参数顺序一致
    # sub_thread = threading.Thread(target=show_info, args=('张三', 23))

    # 以字典的方式传参﹐要保证字典里面的key和函数的参数名保持一致
    sub_thread = threading.Thread(target=show_info, kwargs={'name': '张三', 'age': 23})
    sub_thread.start()
