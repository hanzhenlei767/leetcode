'''
给定一个整数矩阵，找出最长递增路径的长度。

对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。

示例 1:

输入: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
输出: 4 
解释: 最长递增路径为 [1, 2, 6, 9]。
示例 2:

输入: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
输出: 4 
解释: 最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
'''


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