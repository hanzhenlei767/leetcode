class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        #创建二维数组时注意里侧的是创建行,外侧是创建列,并且需要加一
        # dp[i][j] to be true if s[0..i) matches p[0..j) and false otherwise
        #dp的下标与s,p差1
        dp = [[False] * (n+1) for _ in range(m+1)]
        #初始状态,很重要
        dp[0][0] = True
        for i in range(0, m+1):
            for j in range(1, n+1):
            #三种情况 分析模式p最后一位
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-2] or ( i>0 and (s[i-1] == p[j-2] or p[j-2] == '.') and dp[i-1][j])
                else:
                    dp[i][j] = i>0 and dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '.')
        return dp[m][n]