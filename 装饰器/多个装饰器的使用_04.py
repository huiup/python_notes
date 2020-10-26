#  coding:utf-8


def add_p(func):
    def inner():
        result = "<p>" + func() + "</p>"
        return result
    return inner


def add_div(func):
    def inner():
        result = "<div>" + func() + "</div>"
        return result
    return inner

# 多个装饰器的过程：由内到外（先执行内部，再执行外部）
# 即：add_p(add_div(content))
@add_p
@add_div
def content():
    return '给字符串添加标签'


if __name__ == '__main__':
    print(content())
