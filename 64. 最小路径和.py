class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])
        if cols == 0:
            return 0
        #动态规划，构建DP矩阵
        dp = grid
        for i in range(1,rows):
            dp[i][0] = dp[i-1][0]+dp[i][0]
        for j in range(1,cols):
            dp[0][j] = dp[0][j-1]+dp[0][j]
            
        for i in range(1,rows):
            for j in range(1,cols):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + dp[i][j]
        return dp[rows-1][cols-1]