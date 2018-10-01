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