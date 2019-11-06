# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        a,b,c = 0,0,0
        
        if root.left:
            if root.left.left == None and root.left.right == None:
                a = root.left.val
            else:
                b = self.sumOfLeftLeaves(root.left)
        
            
        if root.right:
            c = self.sumOfLeftLeaves(root.right)
            
        return a+b+c