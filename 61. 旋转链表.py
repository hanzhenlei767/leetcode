
'''
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return head
        if head.next == None:
            return head
        if k == 0:
            return head
        
        temp = head
        count = 0
        while temp:
            temp = temp.next
            count += 1
        if k%count >0:
            new_head = self.rotate1step(head)
            for i in range(1,k%count):
                new_head = self.rotate1step(new_head)
            return new_head
        else:
            return head
        
    def rotate1step(self,head):
        old_head = head
        
        while head.next.next:
            head = head.next
            
        new_head = head.next
        new_head.next = old_head
        
        head.next = None

        return new_head
        