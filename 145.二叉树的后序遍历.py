


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#递归
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            a = self.postorderTraversal(root.left)
            b = self.postorderTraversal(root.right)
            return a+b+[root.val]
        else:
            return []

#递推
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        stack1 = [root]
        stack2 = []
        
        while stack1:
            node = stack1.pop()
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
            stack2.append(node.val)
        return stack2[::-1]













