'''
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

'''
#使用栈储存两层的节点。循环打印
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        ret,stack = [],[root]
        tmp_stack = []
        tmp_ret = []
        last_ret = []
        while stack != [] or tmp_stack != []: #上一次和下一层栈全为空时退出
            while stack != []:
                temp = stack.pop()
                tmp_ret.append(temp.val)
                if temp.left:
                    tmp_stack.append(temp.left)
                if temp.right:
                    tmp_stack.append(temp.right)

            last_ret.append(tmp_ret)
            tmp_ret = []
            stack = tmp_stack[::-1]
            tmp_stack = []
        return last_ret



