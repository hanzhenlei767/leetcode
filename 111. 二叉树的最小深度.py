# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        if (root.left == None) & (root.right == None):
            return 1
        if root.left != None:
            d1 = self.minDepth(root.left)
        if root.right != None:
            d2 = self.minDepth(root.right)
        if (root.left != None) & (root.right != None):
            return min(d1+1,d2+1)
        elif root.left != None:
            return d1+1
        else:
            return d2+1
        