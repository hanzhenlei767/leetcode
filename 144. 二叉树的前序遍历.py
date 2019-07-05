# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#递归
class Solution(object):
    
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def f(r,l):
            if r != None:
                l.append(r.val)
            else:
                return None
            if r.left != None:
                f(r.left,l)
            if r.right != None:
                f(r.right,l)
        l = []
        f(root,l)
        return l


#非递归
class Solution(object):
    
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret, stack = [], [root]

        while stack:
            node = stack.pop()
            if node:
                ret.append(node.val)
                #注意压入栈的顺序,先压入右孩子，再压入左孩子
                stack.append(node.right)
                stack.append(node.left)
        return ret