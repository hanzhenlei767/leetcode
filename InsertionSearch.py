
# coding: utf-8

# In[31]:



#升序排列，插值查找

class Solution:
    def InsertionSearch(self, data_list,value):
        if (value>data_list[-1]) | (value<data_list[0]):
            return False
        if data_list == []:
            return False
        mid = ((value - data_list[0])*(len(data_list)-1))//(data_list[-1]-data_list[0])
        if data_list[mid] == value:
            return True
        elif data_list[mid] > value:
            return self.InsertionSearch(data_list[:mid],value)
        else:
            return self.InsertionSearch(data_list[mid+1:],value)

a = Solution()
v = [1,2,3,4,5,6,7,8,9]
a.InsertionSearch(v,5)      
        

