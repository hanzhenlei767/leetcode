'''
解题思路：

题目只给了 要删除的节点(非末尾)    

非末尾 表明我们可以通过node 找到 下一个节点，不需要判断node为空

由于没有办法得到node的前节点，

我们只能通过将  下一个节点的值  复制到  当前节点node，然后移除node的下一个节点来达到目的。
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        next_node = node.next
        node.val = next_node.val
        node.next = next_node.next