'''
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
'''


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