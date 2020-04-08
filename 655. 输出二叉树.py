'''
在一个 m*n 的二维字符串数组中输出二叉树，并遵守以下规则：

行数 m 应当等于给定二叉树的高度。
列数 n 应当总是奇数。
根节点的值（以字符串格式给出）应当放在可放置的第一行正中间。根节点所在的行与列会将剩余空间划分为两部分（左下部分和右下部分）。你应该将左子树输出在左下部分，右子树输出在右下部分。左下和右下部分应当有相同的大小。即使一个子树为空而另一个非空，你不需要为空的子树输出任何东西，但仍需要为另一个子树留出足够的空间。然而，如果两个子树都为空则不需要为它们留出任何空间。
每个未使用的空间应包含一个空的字符串""。
使用相同的规则输出子树。
示例 1:

输入:
     1
    /
   2
输出:
[["", "1", ""],
 ["2", "", ""]]
示例 2:

输入:
     1
    / \
   2   3
    \
     4
输出:
[["", "", "", "1", "", "", ""],
 ["", "2", "", "", "", "3", ""],
 ["", "", "4", "", "", "", ""]]
示例 3:

输入:
      1
     / \
    2   5
   / 
  3 
 / 
4 
输出:
[["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
 ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
 ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
 ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]

'''

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        import math
        
        def dfs(root, h):
            if root:
                return max(dfs(root.left,h+1), dfs(root.right,h+1))
            else :
                return h
        
        height = dfs(root, 0)#高度
        width = 2 ** height -1#宽度
        
        # 初始化
        res = [ ["" for j in range(width)] for i in range(height)]
        
        # dfs print
        def dfs_print(res,root,h,pos):#res:二维数组,root:根节点，h:层数,pos:待填充位置
            if root:
                res[h - 1][pos] = '%d' % root.val
                dfs_print(res, root.left, h+1, pos-2**(height - h - 1))
                dfs_print(res, root.right, h+1, pos+2**(height - h - 1))
        dfs_print(res,root,1,width/2)
        return res