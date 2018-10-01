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
                