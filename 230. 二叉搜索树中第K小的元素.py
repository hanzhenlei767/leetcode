#非递归二叉树中序遍历求解二叉搜索树的第K小元素

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        count = 0
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                count += 1
                if count == k:
                    return node.val
                root = node.right


#递归二叉树返回元素个数求解二叉搜索树的第K小元素

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def count(root):
            if root == None:
                return 0
            return count(root.left)+count(root.right)+1
        num = count(root.left)
        if num == k-1:
            return root.val
        if num > k-1:
            return self.kthSmallest(root.left,k)
        return self.kthSmallest(root.right,k-num-1)




