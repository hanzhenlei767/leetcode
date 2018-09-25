# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        count = 0
        list_Node = []
        while head != None:
            list_Node.append(head)
            head = head.next
        list_len = len(list_Node)
        if list_len == 0:
            return None
        nk = list_len//k
        sk = list_len%k
        if nk > 0:
            for i in range(nk):
                list_Node[i*k:i*k+k] = list_Node[i*k:i*k+k][::-1]
                
            last_Node = list_Node[0]
            for i in range(nk):
                for j in range(k):
                    try:
                        list_Node[i*k+j].next = list_Node[i*k+j+1]
                    except:
                        list_Node[i*k+j].next = None
            return last_Node
        else:
            return list_Node[0]
                