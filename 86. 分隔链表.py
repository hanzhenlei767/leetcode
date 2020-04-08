'''
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。

示例:

输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        
        
        #异常值判断
        if (head == None):
            return head
        if (head.next == None):
            return head
        
        min_list = ListNode(0)
        min_list_head = min_list
        
        max_list = ListNode(0)
        max_list_head = max_list
        
        while head != None:
            if head.val<x:
                min_list.next = head
                min_list = min_list.next
            else:
                max_list.next = head
                max_list = max_list.next
            head = head.next
        max_list.next = None
        min_list.next = None
        
        min_list.next = max_list_head.next
        return_list = min_list_head.next
        return return_list