'''
栈
特性：先入后出

Stack()创建一个空的新栈。它不需要参数，并返回一个空栈。
push(item)将一个新项添加到栈的顶部。它需要item做参数并不返回任何内容。
pop()从栈中删除顶部项。它不需要参数并返回item。栈被修改。
peek()从栈返回顶部项，但不会删除它。不需要参数。不修改栈。
isEmpty())测试栈是否为空。不需要参数，并返回布尔值。
size()返回栈中的item数量。不需要参数，并返回一个整数。
'''
class Stack(object):
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):#返回栈顶元素下标
        return len(self.items)-1
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
if __name__ == '__main__':
    
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())
    print(s.pop())
    print(s.pop())
