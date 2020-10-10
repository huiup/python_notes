#  coding:utf-8
import multiprocessing

# 创建子进程其实是对主进程资源进行拷贝，
# 子进程其实就是主进程的一个副本
g_list = []


def add_data():
    for i in range(3):
        g_list.append(i)
        print('add:', i)
    print('add:', g_list)


def read_data():
    print('read:', g_list)


# 对于linux和mac主进程执行的代码不会进程拷贝﹐但是对应window系统来说主进程执行的代码也会进行拷贝
# 所以需要使用if __name__ == '__main__':，否则会报错
if __name__ == '__main__':
    add_process = multiprocessing.Process(target=add_data)
    read_process = multiprocessing.Process(target=read_data)

    print(' 全局alist:', g_list)
    add_process.start()
    add_process.join()  # 当前进程（主进程）等待添加数据的进程(add_process)执行完成以后代码再继续往下执行
    read_process.start()
