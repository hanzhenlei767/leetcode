
'''
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]
'''

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