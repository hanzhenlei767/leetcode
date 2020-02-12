'''
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
'''

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = []
        lens = len(s)

        if lens < 2:
            return 0


        # initialize dp lisSt
        j = 0
        while j < lens:
            dp.append(0)
            j += 1

        i = 1
        while i < lens:
            if s[i] == ")" and s[i - 1] == "(":
                dp[i] = dp[i - 2] + 2

            if s[i] == s[i - 1] == ")":
                if i - dp[i-1] - 1 >= 0:
                    if s[i - dp[i - 1] - 1] == "(":
                        dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
            i += 1

        return max(dp)