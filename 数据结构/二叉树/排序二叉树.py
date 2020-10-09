'''
排序二叉树
    -深度遍历的中序遍历作用于排序二叉树中，可以得到有序集合
'''

class Node(object):
    def __init__(self,item):
        self.item = item
        self.left = None
        self.right = None


class SortTree(object):
    def __init__(self):
        self.root = None
    def add(self,item):# 将节点插入到排序二叉树中
        node = Node(item)
        # 树为空时
        if self.root == None:
            self.root = node
            return
        cur = self.root
        # 树为非空
        while True:
            if cur.item > item:# 插入值小于根节点时，插入到根节点的左侧
                if cur.left == None:# 左节点为空，则直接插入
                    cur.left = node
                    break
                else:# 左节点非空
                    cur = cur.left
            else:# 插入值大于等于根节点时，插入到根节点的右侧
                if cur.right == None:
                    cur.right = node
                    break
                else:
                    cur = cur.right

    def middle(self,root):# 中序遍历(左根右)
        if root == None:
            return
        self.middle(root.left)
        print(root.item)
        self.middle(root.right)

if __name__ == '__main__':
    alist = [3,8,5,7,6,2,1]
    tree = SortTree()
    for item in alist:
        tree.add(item)
    tree.middle(tree.root)


        
