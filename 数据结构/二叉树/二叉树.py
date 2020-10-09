'''
二叉树
-根节点:树中上部的节点
-左叶子节点
-右叶子节点
-子树
    -完整的子树
        -一个根节点，左右叶子节点组成
    -不完整的子树
        -根节点，左叶子节点
        -根节点，右叶子节点
        -根节点
            特点︰每一个节点都可以作为某一颗子树的根节点
'''
class Node(object):
    def __init__(self,item):
        self.item = item
        self.left = None #指向该节点的左叶子节点
        self.right = None #指向该节点的右叶子节点

class Tree(object):
    def __init__(self): # 构建空树
        self.root = None # 永远指向二叉树的根节点
    def insert(self,item):# 自上向下从左到右的准则插入新的节点
        node = Node(item)
        if self.root == None:# 如果树为空
            self.root = node
            return
        cur = self.root# 如果树为非空
        q = [cur]
        while True:
            n = q.pop(0)
            if n.left != None:
                q.append(n.left)
            else:
                n.left = node
                break
            if n.right != None:
                q.append(n.right)
            else:
                n.right = node
                break
    
    def travel(self):# 广度遍历（横向）：自上向下逐行遍历
        cur = self.root
        q = [cur]
        while q:
            n = q.pop(0)
            print(n.item)
            if n.left != None:
                q.append(n.left)
            if n.right != None:
                q.append(n.right)
# 
#   深度遍历
#     - 纵向遍历。
#     - 前、中、后序遍历形式需要作用到子树中。
#         - 前序：根左右
#         - 中序：左根右
#         - 后序：左右根

    # 前序遍历(根左右)
    def forward(self,root):# 参数root表示的是子树的根节点，需要给递归调用的forward传入不同子树的根节点
        if root == None:
            return
        print(root.item)
        self.forward(root.left)
        self.forward(root.right)
    def middle(self,root):# 中序遍历(左根右)
        if root == None:
            return
        self.middle(root.left)
        print(root.item)
        self.middle(root.right)
    def back(self,root):# 后序遍历(左右根) 
        if root == None:
            return
        self.back(root.left)
        self.back(root.right)
        print(root.item)


if __name__ == '__main__':
    tree = Tree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)
    tree.insert(6)
    tree.insert(7)
    # tree.forward(tree.root)
    # tree.middle(tree.root)
    tree.back(tree.root)



