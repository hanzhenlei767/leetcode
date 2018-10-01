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
        