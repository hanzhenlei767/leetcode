'''
给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。

示例 1:
给定的树 s:

     3
    / \
   4   5
  / \
 1   2
给定的树 t：

   4 
  / \
 1   2
返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。
'''


#两重递归方法

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s == None:
            return False
        elif self.isSame(s,t) == True:
            return True
        else:
            return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)


    def isSame(self,s,t):
        if s == None and t == None:
            return True
        elif s == None or t == None:
            return False
        elif s.val != t.val:
            return False
        else:
            return self.isSame(s.left,t.left) and self.isSame(s.right,t.right)
			
#递归前序遍历是否包含方法
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        def pre_order(root, res):
            """
            获得二叉树的前序遍历结果
            :param root:  二叉树根节点
            :param res: 结果存储列表
            :return:
            """
            if root:                            # 如果当前节点不为空
                res.append(str(root.val))       # 添加当前结点的值
                pre_order(root.left, res)       # 左子树的前序遍历
                pre_order(root.right, res)      # 右子树的前序遍历
            else:                               # 如果当前结点为空
                res.append('#')                 # 用“#”代替

        s_list, t_list = [], []                 # 序列化结果存储器
        pre_order(s, s_list)                    # 获取s的前序遍历结果
        pre_order(t, t_list)                    # 获取t的前序遍历结果
        # print(','.join(t_list))
        # print(','.join(s_list))
        # 将列表转为字符串进行比较，前端加“，”防止出现“2,#,#”in“12,#,#”中的情况
        return ','+','.join(t_list) in ','+','.join(s_list)
		
#递推前序遍历是否包含方法
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        def pre_order(root,ret):
            """
            :type root: TreeNode
            :rtype: List[int]
            """
            stack =[root]

            while stack:
                node = stack.pop()
                if node:
                    ret.append(str(node.val))
                    #注意压入栈的顺序,先压入右孩子，再压入左孩子
                    stack.append(node.right)
                    stack.append(node.left)
                else:
                    ret.append('#')

        s_list, t_list = [], []                 # 序列化结果存储器
        pre_order(s, s_list)                    # 获取s的前序遍历结果
        pre_order(t, t_list)                    # 获取t的前序遍历结果
        # print(','.join(t_list))
        # print(','.join(s_list))
        # 将列表转为字符串进行比较，前端加“，”防止出现“2,#,#”in“12,#,#”中的情况
        return ','+','.join(t_list) in ','+','.join(s_list)