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