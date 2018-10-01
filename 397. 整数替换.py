
#递归

class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 0
        if n % 2 == 0:
            return 1 + self.integerReplacement(n / 2)
        else:
            return 1 + min(self.integerReplacement(n + 1), self.integerReplacement(n - 1))

#位运算。

#当n是奇数的时候，如何决定应该加1还是减1？我们可以看这个数字的二进制。
#奇数的二进制一定是01或11结尾。
#同时，发现如果把一个奇数化为4的倍数，变成1的步骤会更少（3除外）。
class Solution:
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n > 1:
            count += 1
            if n & 1:#奇数
                if n & 2 and n != 3:#尾号是11
                    n += 1
                else:#尾号是01
                    n -= 1
            else:#偶数
                n >>= 1
        return count
