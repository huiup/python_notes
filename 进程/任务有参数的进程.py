#  coding:utf-8

import multiprocessing


# 显示信息的任务
def show_info(name, age):
    print(name, age)


if __name__ == '__main__':
    # 创建子进程

    # 1.以元组方式传参，参数顺序得一致
    # sub_process = multiprocessing.Process(target=show_info, args=('张三', 23))

    # 2.以字典方式传参,顺序没要求，但key要与形参保持一致
    # sub_process = multiprocessing.Process(target=show_info, kwargs={'name': '张三', 'age': 23})

    # 3.混合方式传参
    sub_process = multiprocessing.Process(target=show_info, args=('张三',), kwargs={'age': 23})
    # 启动进程
    sub_process.start()
