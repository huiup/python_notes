'''
双端队列：
同队列相比，有两个头部和尾部。可以在双端进行数据的插入和删除，提供了单数据结构中栈和队列的特性
Deque()创建一个空的新deque。它不需要参数，并返回空的deque。
addFront(item)将一个新项添加到deque 的首部。它需要item 参数并不返回任何内容。
addRear(item)将一个新项添加到deque的尾部。它需要item 参数并不返回任何内容。
removeFront()从 deque 中删除首项。它不需要参数并返回item。deque被修改。
removeRear()从deque中删除尾项。它不需要参数并返回item。deque被修改。
isEmpty()测试deque是否为空。它不需要参数，并返回布尔值。
size()返回deque中的项数。它不需要参数，并返回一个整数。
'''
class Deque():
    def __init__(self):
        self.items = []
    def addFront(self,item):
        self.items.append(item)
    def addRear(self,item):
        self.items.insert(0,item)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)

'''
双端队列应用案例:回文检查
    -回文是一个字符串，读取首尾相同的字符，例如，radar toot madam。
'''
def check(arg):
    #创建一个双端队列，将字符串中的字符依次添加到双端队列中
    deque = Deque()
    for char in arg:
        deque.addRear(char)
        # deque.addRear(char)
    Equal = True
    #当至少有一个字符并且满足收尾相等则循环
    while deque.size() > 1 and Equal:
        first = deque.removeFront()
        last = deque.removeRear()
        if first != last:
            Equal = False
    return Equal

if __name__ == '__main__':
    
    print(check("zhangnahz"))
    print(check("radar"))
    print(check("tomakmot"))
