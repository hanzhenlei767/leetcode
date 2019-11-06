# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        
        def func(root):
            temp_list = []
            if root == None:
                return temp_list
            if root.left == None and root.right == None:
                temp_list.append(root.val)
                
            temp_list.extend(func(root.left))
            temp_list.extend(func(root.right))
            return temp_list
        
        if func(root1) == func(root2):
            return True
        return False