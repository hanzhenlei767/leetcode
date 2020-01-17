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