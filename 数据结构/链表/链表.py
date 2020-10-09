class Node(object):
    def __init__(self,item):
        self.item = item
        self.next = None

class Link(object):
    def __init__(self):
        self._head = None# _head永远要指向链表中的第一个节点，None表示链表中没有节点
    def add(self,item):# 添加
        node = Node(item)
        node.next = self._head
        self._head = node # 将_head指向当前节点
    def travel(self):# 链表遍历
        cur = self._head# cur指向第一个节点,_head要永远指向第一个节点，轻易不要修改_head的指向
        while cur:
            print(cur.item)
            cur = cur.next
    def is_Empty(self):# 判空
        return self._head == Node
    def length(self):# 链表长度
        cur = self._head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        return count
    def append(self,item):# 向链表的尾部添加节点
        node = Node(item)
        if self._head == None:# 如果链表为空
            self._head = node
            return
        # 如果链表非空
        pre = None # pre是指向cur的前一个节点
        cur = self._head 
        while cur:
            pre = cur
            cur = cur.next
        pre.next = node# 当循环结束后，pre指向链表中最后一个节点,cur为空 
    def search(self,item):# 查找节点
        cur = self._head
        find = False
        while cur:
            if cur.item == item:
                find = True
                break
            else:
                cur = cur.next
        return find
    def insert(self,pos,item):# 指定位置插入（pos不能超过链表长度）
        node = Node(item)
        pre = None
        cur = self._head
        if pos == 0:# 特殊处理插入位置为0的情况
            node.next = self._head
            self._head = node
            return
        # 非0的情况
        for i in range(pos):
            pre = cur
            cur = cur.next
        pre.next = node
        node.next = cur
    def remove(self,item):# 删除指定元素的节点
        if self._head.item == item:# 特殊处理第一个节点
            self._head = self._head.next
            return
        pre = None
        cur = self._head
        while cur:
            pre = cur
            cur = cur.next
            if cur.item == item:
                pre.next = cur.next
                return
    def reverse(self):# 链表倒置
        pre = self._head
        cur = pre.next
        next_node = cur.next
        
        pre.next = None# 链表倒置后，pre就是最后一个节点，最后一个节点的next指向None
        while True:
            cur.next = pre
            # 依次将pre，cur，next_node向后偏移
            pre = cur
            cur = next_node
            if next_node != None:
                next_node = next_node.next
            else:
                break
        self._head = pre

if __name__ == '__main__':
    link = Link()
    link.append(1)
    link.append(2)
    link.append(3)
    link.append(4)
    # link.remove(1)
    # link.travel()
    # link.insert(0,1.2)
    # link.travel()
    # print(link.search(1))
    # print(link.length())
    link.reverse()
    link.travel()
