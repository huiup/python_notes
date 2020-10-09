'''
队列
特性：先进先出

Queue()创建一个空的新队列。它不需要参数，并返回一个空队列。
enqueue(item)将新项添加到队尾。它需要item作为参数，并不返回任何内容。
dequeue()从队首移除项。它不需要参数并返回item。队列被修改。
isEmpty()查看队列是否为空。它不需要参数，并返回布尔值。
size()返回队列中的项数。它不需要参数，并返回一个整数。
'''
class Queue(object):
    def __init__(self):
        self.items = []
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)


'''
案例:烫手的山芋
烫手山芋游戏介绍∶6个孩子围城一个圈，排列顺序孩子们自己指定。第一个孩子手里有一个烫手的山芋，需要在计时器
计时1秒后将山芋传递给下一个孩子，依次类推。规则是，在计时器每计时7秒时，手里有山芋的孩子退出游戏。该游戏
直到剩下一个孩子时结束，最后剩下的孩子获胜。请使用队列实现该游戏策略，排在第几个位置最终会获胜。

分析：
在一轮游戏中山芋会被传递6次
山芋传递的次数不受孩子个数的影响
山芋传递六次后一轮游戏结束，淘汰一个孩子游戏继续
队列:先进先出，只可以从对头取元素，从队尾添加元素。
准则:保证队头孩子手里面有山芋（谁手里有山芋谁作为队头)
方便删除元素。最终7秒到的时候需要将手里有山芋的孩子从队列中剔除。

'''
if __name__ == '__main__':
    # s = Queue()
    # s.enqueue(1)
    # s.enqueue(2)
    # s.enqueue(3)
    # print(s.dequeue())
    # print(s.dequeue())
    # print(s.dequeue())

    kids = ['A','B','C','D','E','F']
    queue = Queue()
    for kid in kids:
        queue.enqueue(kid)
    while(queue.size() > 1):# 剩下1个孩子时结束
        for i in range(6):# 山芋传递次数
            kid = queue.dequeue()# 队头孩子出队列再入队列
            queue.enqueue(kid)
        queue.dequeue()# 一轮游戏结束后，将队头的孩子淘汰
    print('获胜者：',queue.dequeue())