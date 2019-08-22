#斐波那契数列
class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 0
        if N == 1:
            return 1
        
        a = [0,1]
        for i in range(2,N+1):
            a.append(a[i-1]+a[i-2])
        return a[-1]
        