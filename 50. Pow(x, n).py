
'''
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
说明:

-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。

'''




class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x==0:
            return 0
        if n == 0:
            return 1
        
        elif n<0:
            result = self.pow_x_n(x,-n)
            return 1.0/result
        else:
            return self.pow_x_n(x,n)
        
    def pow_x_n(self,x,n):
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n == 1:
            return x
        if n%2 == 0:
            result = self.pow_x_n(x,n2>>1)
            return result*result
        else:
            result = self.pow_x_n(x,(n-1)>>1)
            return result*result*x
        