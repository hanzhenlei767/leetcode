'''
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false
'''


#思路1：
#每行使用二分查找，仅利用了行有序。
#思路2：
#从右上角查起，若果target>元素，则row++；如果target<元素，则col--.
#思路3：
#思路1和思路2结合下，二分查找搜索列，再二分查找搜索行。


#思路2：
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        rows = len(matrix)
        cols = len(matrix[0])-1
        row = 0
        while row < rows and cols >= 0:
            if matrix[row][cols] == target:
                return True
            elif matrix[row][cols] > target:
                cols -= 1
            else:
                row += 1
        return False







class Solution:
    def searchMatrix(self, matrix, target):
        """
        按行查找
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0:
            return False
        if len(matrix[0]) == 0:
            return False
        for i in range(len(matrix)):
            if (matrix[i][0] > target):#起始大于target,查找失败
                return False
            if (matrix[i][len(matrix[i])-1] < target):#结尾小于target，查找失败
                continue
            if self.find_target(matrix[i],target) == True:
                return True
        return False

    def find_target(self,find_list,target):
        '''
        二分查找
        '''
        head = 0
        tail = len(find_list) - 1
        while head<=tail:
            mid = (head+tail)//2
            if find_list[mid] < target:
                head = mid + 1
            elif find_list[mid] > target:
                tail = mid - 1
            else:
                return True
        return False