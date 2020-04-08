'''
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
示例 1:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
输出: true
示例 2:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
输出: false

'''

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        if len(matrix[0]) == 0:
            return False
        
        for i in range(len(matrix)):
            if matrix[i][len(matrix[i])-1] >= target:
                return self.find_target(matrix[i],target)
        return False

    def find_target(self,find_list,target):
        head = 0
        tail = len(find_list) - 1
        while head <= tail:
            mid = (head+tail)//2
            if find_list[mid] > target:
                tail = mid-1
            elif find_list[mid] < target:
                head = mid+1
            else:
                return True
        return False