def leaf(self,root):
        if root==None:
            return 0 #当二叉树为空时直接返回0
        elif root.left==None and root.right==None:
            return 1 #当二叉树只有一个根，但是无左右孩子时，根节点就是一个叶子节点
        else:
            return (self.leaf(root.left)+self.leaf(root.right))