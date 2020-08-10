'''
给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

示例 1:

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
说明: 你可以假设 n 不小于 2 且不大于 58。
'''

class Solution(object):
    def __init__(self):
        self._dict = {}

    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        if n in self._dict:
            return self._dict[n]
        res = -1
        for i in range(1, n):
            res = max(res, max(i * (n - i), i * self.integerBreak(n - i)))
        self._dict[n] = res
        return res

