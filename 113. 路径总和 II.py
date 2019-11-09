# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum_):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        
        last_list = []
        sum_list = []
        
        def func(root,sum_list,sum_):
            last_list = []
            if root.left == None and root.right == None and (sum(sum_list)+root.val)== sum_:
                last_list.append(sum_list+[root.val])
                return last_list
            if root.left:
                last_list.extend(func(root.left,sum_list+[root.val],sum_))
            if root.right:
                last_list.extend(func(root.right,sum_list+[root.val],sum_))
            return last_list
        
        
        return func(root,sum_list,sum_)