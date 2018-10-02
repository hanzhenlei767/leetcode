# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        
        fast_p = head
        slow_p = head
        
        while fast_p != None and fast_p.next != None:
            fast_p = fast_p.next.next
            slow_p = slow_p.next
            if fast_p == slow_p:
                return True
        return False