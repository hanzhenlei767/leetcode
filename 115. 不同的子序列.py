
'''
给定一个字符串 S 和一个字符串 T，计算在 S 的子序列中 T 出现的个数。

一个字符串的一个子序列是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）

题目数据保证答案符合 32 位带符号整数范围。

 

示例 1：

输入：S = "rabbbit", T = "rabbit"
输出：3
解释：

如下图所示, 有 3 种可以从 S 中得到 "rabbit" 的方案。
(上箭头符号 ^ 表示选取的字母)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
示例 2：

输入：S = "babgbag", T = "bag"
输出：5
解释：

如下图所示, 有 5 种可以从 S 中得到 "bag" 的方案。 
(上箭头符号 ^ 表示选取的字母)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
'''
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if s == '' or t == '':
            return 0
        LS = len(s)
        LT = len(t)
        a = [[0 for _ in range(LS)] for _ in range(LT)]
        if s[0] == t[0]:
            a[0][0] = 1
        for i in range(1, LS):
            if s[i] == t[0]:
                a[0][i] = a[0][i - 1] + 1
            else:
                a[0][i] = a[0][i - 1]
        for i in range(1, LT):
            for j in range(1, LS):
                if s[j] == t[i]:
                    a[i][j] = a[i - 1][j - 1] + a[i][j - 1]
                else:
                    a[i][j] = a[i][j-1]
        return a[LT-1][LS-1]
		
		
		
		
		
		