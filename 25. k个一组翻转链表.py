'''
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例 :

给定这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5

说明 :

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
'''

#链表方法

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
        #统计链表个数
        temp_head = head
        count = 0
        while temp_head:
            temp_head = temp_head.next
            count += 1
        #链表总个数小于每组的个数，直接返回元链表
        if count < k:
            return head
        
        #将链表分段
        head_list = []
        next_head = head
        for i in range(0,count//k):
            head_list.append(next_head)
            #查找下一组链表头
            index = 0
            while index<k:
                next_head = next_head.next
                index += 1
   
        for i in head_list:
            print(i.val)
        #取出翻转后的表头
        new_head = self.reverseList(head_list[0],k)
        return_val = new_head
        for i in range(len(head_list)-1):
            temp = head_list[i]
            while temp.next:
                temp = temp.next
            temp.next = self.reverseList(head_list[i+1],k) 
            
        if count%k != 0:
            temp = head_list[-1]
            while temp.next:
                temp = temp.next
            temp.next = next_head
        
        return return_val
        '''
        while return_val:
            print(return_val.val)
            return_val = return_val.next
        '''
    def reverseList(self,head,k):

        p1 = head
        p2 = head.next
        count = 1
        while count<k:
            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3
            count += 1
        head.next = None
        return p1
   
   
   
 #list处理链表方法

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
                