#链表解题方法

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return head
        
        #若首节点等于val
        while head.val == val:
            head = head.next
            if head == None:
                return head
        
        temp = head
        
        #非首节点
        while temp.next:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head
                
            
        



#转换成list解法

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return None
        list_head = []
        while head:
            if head.val != val:
                list_head.append(head)
            head = head.next
        if list_head == []:
            return None
        return_list = list_head[0]
        for i in range(len(list_head)):
            try:
                list_head[i].next = list_head[i+1]
            except:
                list_head[i].next = None
        return return_list