
# coding: utf-8

# In[19]:



#降序排列，二分查找

class Solution:
    def BinarySearch(self, data_list,value):
        if data_list == []:
            return False
        mid = (len(data_list) - 1)//2
        if data_list[mid] == value:
            return True
        elif data_list[mid] < value:
            return self.BinarySearch(data_list[:mid],value)
        else:
            return self.BinarySearch(data_list[mid+1:],value)

a = Solution()
v = [9,8,7,6,5,4,3,2,1,0]
a.BinarySearch(v,12)      
        


# In[18]:




