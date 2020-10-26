#  coding:utf-8

# 装饰器的功能特点;
# 1. 不修改已有函数的源代码
# 2. 不修改已有函数的调用方式
# 3. 给已有函数增加额外的功能

# 定义装饰器
def decorator(func):  # 如果闭包函数的参数有且只有一个并且是函数类型﹐那么这个闭包函数称为装饰器
    def inner():
        print('已添加登录验证！')
        func()

    return inner


# 装饰器的语法糖写法:@装饰器名称﹐装饰器的语法糖就是在装饰以后函数的写法更加简单
@decorator  # comment = decorator(comment)装饰器语法糖对该代码进行了封装
def comment():
    print('发表评论')


if __name__ == '__main__':
    # 1.普通写法
    # comment = decorator(comment)
    # comment()

    comment()
