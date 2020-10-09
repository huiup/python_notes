# coding:utf-8
import multiprocessing
import time


'''
Process([group [target [, name [,args [,kwargs]]]])
group:进程组,目前只能使用None ，一般不需要设置
target:进程执行的目标任务(多为函数)
name:进程名,如果不设置,默认是Process-l,2,3,4...
args∶以元组方式给执行任务传参
kwargs:以字典方式给执行任务传参
'''

# 创建子进程（自己手动创建的进程称为子进程)
def dance():
    for i in range(3):
        print('跳舞中。。。')
        time.sleep(0.2)
def sing():
    for i in range(3):
        print('唱歌中。。。')
        time.sleep(0.2)

if __name__ == '__main__':
    # 1:主进程创建两个子进程
    # dance_process = multiprocessing.Process(target=dance)
    # sing_process = multiprocessing.Process(target=sing)
    # dance_process.start()
    # sing_process.start()

    # 2:一主一子
    # 子进程执行跳舞
    dance_process = multiprocessing.Process(target=dance)
    dance_process.start()
    # 主进程执行唱歌
    sing()


