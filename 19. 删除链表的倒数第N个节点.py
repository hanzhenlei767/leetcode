#链表解决方法

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp_head = head
        count = 0
        while temp_head:
            temp_head = temp_head.next
            count += 1
        
        #共count个节点,删除倒数第n个就是删除整数第count-n+1个
        if count-n == 0:
            return head.next
        else:
            temp_head = head
            index = 1
            while index != (count -n):
                temp_head = temp_head.next
                index += 1
            #找到了被删除节点的前一个节点
            temp_head.next = temp_head.next.next
        return head



#链表问题转换成list解决办法

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        List = []  
        count = 0  
        while(head):  
            List.append(head)  
            head=head.next  
            count = count+1  
          
        if count==1:  
            return None  
        if List[-n].next==None:  
            List[-n-1].next = None  
            return List[0]  
        else:  
            List[-n].val = List[-n].next.val  
            List[-n].next = List[-n].next.next  
        return List[0]