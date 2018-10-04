# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return root
        if (root.left == None) & (root.right == None):
            return root
        
        temp = root.left
        root.left = root.right
        root.right = temp
        
        if root.left != None:
            self.invertTree(root.left)
        if root.right != None:
            self.invertTree(root.right)
        return root