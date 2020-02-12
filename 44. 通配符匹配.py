'''
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "*"
输出: true
解释: '*' 可以匹配任意字符串。
示例 3:

输入:
s = "cb"
p = "?a"
输出: false
解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
示例 4:

输入:
s = "adceb"
p = "*a*b"
输出: true
解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
示例 5:

输入:
s = "acdcb"
p = "a*c?b"
输入: false
'''

#给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
#'?' 可以匹配任何单个字符。
#'*' 可以匹配任意字符串（包括空字符串）。

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m,n = len(s)+1,len(p)+1
        matric = [[0]*n for i in range(m)]#m行,n列
        matric[0][0] = True

        for i in range(1,n):
            if p[i-1] == '*':
                matric[0][i] = matric[0][i-1] 
            else:
                matric[0][i] = False
        for i in range(1,m):
            matric[i][0] = False

        for i in range(1,n):#列
            for j in range(1,m):#行
                if s[j-1] == p[i-1] or p[i-1] == '?':
                    matric[j][i] = matric[j-1][i-1]
                elif p[i-1] == '*':
                    matric[j][i] = matric[j-1][i] or matric[j][i-1] #均可以
                    #matric[j][i] = matric[j-1][i-1] or matric[j-1][i] or matric[j][i-1]
                else:
                    matric[j][i] = False
        return matric[m-1][n-1]