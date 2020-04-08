'''
给定一个正整数 n，你可以做如下操作：

1. 如果 n 是偶数，则用 n / 2替换 n。
2. 如果 n 是奇数，则可以用 n + 1或n - 1替换 n。
n 变为 1 所需的最小替换次数是多少？

示例 1:

输入:
8

输出:
3

解释:
8 -> 4 -> 2 -> 1
示例 2:

输入:
7

输出:
4

解释:
7 -> 8 -> 4 -> 2 -> 1
或
7 -> 6 -> 3 -> 2 -> 1
'''
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
