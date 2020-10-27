#  coding:utf-8
# 一个类只要实现了_enter__()和_exit_()这个两个方法﹐通过该类创建的对象我们就称之为上下文管理器。

# 自定义上下文管理器类
class File(object):
    def __init__(self, file_name, file_mode):
        self.file_name = file_name
        self.file_mode = file_mode

    def __enter__(self):
        # 上文方法﹐负责返回操作对象资源﹐比如︰文件对象﹐数据库连接对象
        self.file = open(self.file_name, self.file_mode)
        return self.file

    # 当with语句执行完成以后自动执行__exit__方法
    def __exit__(self, exc_type, exc_val, exc_tb):
        # 下文方法，负责释放对象资源，比如：关闭文件，关闭数据库连接对象
        self.file.close()
        print('over')


# 即使有错误也能关闭
if __name__ == '__main__':
    with File('1.txt', 'r') as file:
        data = file.read()
        print(data)
