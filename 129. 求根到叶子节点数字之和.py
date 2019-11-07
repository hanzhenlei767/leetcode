# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
            
        def fun(root,num):
            a,b,c = 0,0,0
            if root.left == None and root.right == None:
                c = num
            if root.left:
                a = fun(root.left,num*10+root.left.val)
            if root.right:
                b = fun(root.right,num*10+root.right.val)
            return a+b+c
        return fun(root,root.val)