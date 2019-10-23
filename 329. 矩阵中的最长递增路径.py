def FindPath(matrix,dp,i,j,m,n):
    if dp[i][j] != -1:
        return dp[i][j]
    dp[i][j] = 1
    Next =[[1,0],[-1,0],[0,-1],[0,1]]
    for k in range(4):
        a = i+Next[k][0]
        b = j+Next[k][1]
        if a>=0 and b>=0 and  a<m and b<n and matrix[i][j]>matrix[a][b]:
            dp[i][j] = max(dp[i][j],FindPath(matrix,dp,a,b,m,n)+1)
    return dp[i][j]
	
def longestIncreasingPath(matrix):
    if matrix == []:
        return 0
    m = len(matrix)
    n = len(matrix[0])
    dp = [[-1]*n for _ in range(m)]
    rtn = 1
    for i in range(m):
        for j in range(n):
            rtn = max(rtn,FindPath(matrix,dp,i,j,m,n))
    return rtn
	
nums = [[9,9,4],[6,6,8],[2,1,1]]
longestIncreasingPath(nums)


class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if matrix == []:
            return 0
        def FindPath(matrix,dp,i,j,m,n):
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = 1
            Next =[[1,0],[-1,0],[0,-1],[0,1]]
            for k in range(4):
                a = i+Next[k][0]
                b = j+Next[k][1]
                if a>=0 and b>=0 and  a<m and b<n and matrix[i][j]>matrix[a][b]:
                    dp[i][j] = max(dp[i][j],FindPath(matrix,dp,a,b,m,n)+1)
            return dp[i][j]
        m = len(matrix)
        n = len(matrix[0])
        dp = [[-1]*n for _ in range(m)]
        rtn = 1
        for i in range(m):
            for j in range(n):
                rtn = max(rtn,FindPath(matrix,dp,i,j,m,n))
        return rtn