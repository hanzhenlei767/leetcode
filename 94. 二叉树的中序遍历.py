# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#递归
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def f(root,m_list):
            if root != None:
                f(root.left,m_list)
                m_list.append(root.val)
                f(root.right,m_list)
        l = []
        f(root,l)
        return l
#非递归	
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret, stack = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                temNode = stack.pop()
                ret.append(temNode.val)
                root = temNode.right
        return ret		
