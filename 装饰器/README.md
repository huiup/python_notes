### 装饰器

##### 1.定义

就是给已有函数增加额外功能的函数，它本质上就是一个闭包函数（如果闭包函数的参数有且只有一个并且是函数类型，那么这个闭包函数称为装饰器）

装饰器的功能特点;

1. 不修改已有函数的源代码
2. 不修改已有函数的调用方式
3. 给已有函数增加额外的功能

##### 2.装饰器使用

```python
# 给函数添加统计执行时间功能
def decorator(func):  # 如果闭包函数的参数有且只有一个并且是函数类型﹐那么这个闭包函数称为装饰器
    def inner():
        begin = time.time()
        func()
        end = time.time()
        print('函数执行完成耗时：', end - begin)
    return inner
# 装饰器的语法糖写法:@装饰器名称﹐装饰器的语法糖就是在装饰以后函数的写法更加简单
@decorator # comment = decorator(comment)装饰器语法糖对该代码进行了封装
def work():
    for i in range(10000):
        print(i)
if __name__ == '__main__':
    work()
```

##### 3.装饰带有参数的函数（内部函数有参数）

使用装饰器装饰已有函数的时候，**内部函数的类型和要装饰的已有函数的类型保持一致**

- 带参数的

```python
def decorator(func):
    def inner(a, b):
        print('正在执行加法计算！')
        num = func(a, b)
    return inner
@decorator
def add_num(num1, num2):
    result = num1 + num2
    print('结果为：', result)
if __name__ == '__main__':
    add_num(1, 2)
```

- 带返回值的

```python
def decorator(func):
    def inner(a, b):
        print('正在执行加法计算！')
        num = func(a, b)
        return num
    return inner
@decorator
def add_num(num1, num2):
    result = num1 + num2
    return result
if __name__ == '__main__':
    result = add_num(1, 2)
    print(result)
```

- 不定长参数 (通用装饰器)

```python
def decorator(func):
    def inner(*args, **kwargs):
        print('正在执行加法计算！')
        # *args:把元组里面的每一个元素﹐按照位置参数的方式进行传参
        # **kwargs:把字典里面的每一个键值对﹐按照关键字的方式进行传参
        # 这里对字典进行拆包﹐仅限于结合不定长参数的函数使用
        num = func(*args, **kwargs)
        return num
    return inner
@decorator
def add_num(*args, **kwargs):
    # *args：元组类型
    # **kwargs：字典类型
    result = 0
    for value in args:
        result += value
    for value in kwargs.values():
        result += value
    return result
if __name__ == '__main__':
    result = add_num(1, 2)
    print(result)
```

##### 4.多个装饰器的使用

```python
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
```

执行结果：

```python
<p><div>给字符串添加标签</div></p>
```

##### 5.带有参数的装饰器

```python
# 在装饰器外面再包裹上一个函数，让最外面的函数接收参数，返回的是装饰器，因为@符号后面必须是装饰器实例。
def return_decorator(flag):
    # 装饰器，装饰器只能接收一个参数并且是函数类型
    def decorator(func):
        def inner(a, b):
            if flag == "+":
                print("正在努力执行加法计算")
            elif flag == "-":
                print("正在努力执行减法计算")
            func(a, b)
        return inner
    # 当调用函数的时候可以返回一个装饰器decorator
    return decorator
@return_decorator('+')
def add_num(a, b):
    result = a + b
    print(result)
@return_decorator('-')
def sub_num(a, b):
    result = a - b
    print(result)
if __name__ == '__main__':
    add_num(1, 2)
    sub_num(2, 1)
```

执行结果：

```python
正在努力执行加法计算
3
正在努力执行减法计算
1
```

##### 6.类装饰器

```python
# 类装饰器：使用类装饰已有函数

class MyDecorator(object):
    def __init__(self, func):
        self.__func = func

    # 实现__call_这个方法﹐让对象变成可调用的对象
    def __call__(self, *args, **kwargs):
        # 对已有函数进行封装
        print('嘟！嘟！嘟！')
        self.__func()
@MyDecorator
def show():
    print('咚！咚！咚！')
if __name__ == '__main__':
    # 执行show，相当于执行MyDecorator类创建实例对象-->show()-->对象(),而对象不能直接调用，需要实现__call__方法
    show()
```

