### 生成器

##### 1.介绍
根据程序员制定的规则循环生成数据，当条件不成立时则生成数据结束。

注意：数据不是一次性全部生成，而是使用一个，再生成一个，这样可以节约大量的内存。

##### 2.生成器的创建方式

- **生成器推导式**：把列表推导式中的中括号改成小括号即可

```python
my_generator = (i * 2 for i in range(5))
if __name__ == '__main__':
    # 遍历时，当生成器已经没有值时，会抛出StopIteration，表示生成器生成数据完毕
    # 1.第一种取值
    # value = next(my_generator)
    # print(value)

    # 2.第二种取值
    # while True:
    #     try:
    #         value = next(my_generator)
    #         print(value)
    #     except Exception as e:
    #         break

    # 3.第三种取值（常用）
    # for循环内部循环调用next函数获取生成器中的下一值，当出现异常for循环内部自动进行了异常捕获
    for value in my_generator:
        print(value)
```

- **yield关键字**：只要在函数里面看到有yield关键字，那么这个函数可以认为是一个生成器

```python
# 在函数里面看到有yield关键字﹐那么这个函数就是生成器
def my_generator():
    for i in range(5):
        print('开始生成数据...')
        # 当程序执行到yield关键字的时候代码暂停并把结果返回﹐再次启动生成器的时候会在暂停的位置继续往下执行
        yield i
        print('上一次数据生成完毕!')
if __name__ == '__main__':
    result = my_generator()  # 要先调用
    # 1.普通取值
    # print(next(result))

    # 2.常用取值
    for value in result:
        print(value)
```

3.**生成器使用场景**

生成斐波那契数列

```python
def fibonacci(num):
    # 初始化前两个值
    a = 0
    b = 1
    # 记录每次生成个数的索引
    current_index = 0
    while current_index < num:
        result = a
        # 条件成立，交换两个变量的值
        a, b = b, a + b
        current_index += 1
        yield result
if __name__ == '__main__':
    f = fibonacci(50)
    for value in f:
        print(value)
```

