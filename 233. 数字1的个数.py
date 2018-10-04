class Solution:
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<0:
            return 0
        
        rtn_val = 0
        count = self.calculate_bit_count(n)#计算位数
        if count == 1:
            if n >= 1:
                return 1
            else:
                return 0
        else:
            int_val = self.bit_count_to_int(count)#计算基数
            if n//int_val == 1:
                rtn_val += (self.countDigitOne(int_val-1) + (n%int_val + 1) + self.countDigitOne(n%int_val))
            else:
                rtn_val += (self.countDigitOne(int_val-1)*(n//int_val) + self.countDigitOne(n%int_val) + int_val)
        return rtn_val
    
    #根据数计算位数      
    def calculate_bit_count(self,n):
        count = 1
        temp = n
        while True:
            temp = temp//10
            if temp == 0:
                break
            else:
                count += 1
        return count
    
    #根据位数计算最小的数
    def bit_count_to_int(self,count):
        if count == 0 :
            return 0

        int = 1
        for i in range(count-1):
            int *= 10
        return int
            
        