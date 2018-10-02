# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        
        fast_p = slow_p = head
        while fast_p and fast_p.next:
            fast_p = fast_p.next.next
            slow_p = slow_p.next
            if fast_p == slow_p:
                
                #存在环形链表，计算环形链表个数
                first = fast_p
                count = 1
                while first != fast_p.next:
                    fast_p = fast_p.next
                    count += 1
                #count是环形链表的个数，先让前指针走count步，尾指针再一块走，相遇点即为入口
                head_p = tail_p = head
                for i in range(count):
                    head_p = head_p.next
                while True:
                    if head_p == tail_p:
                        return head_p 
                    head_p = head_p.next
                    tail_p = tail_p.next
                     
        return None