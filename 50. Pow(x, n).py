





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
        