
'''
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。



在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

'''
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            list_result = self.generate(numRows-1)
            temp_list = list_result[-1]
            temp = []
            temp.append(temp_list[0])
            for i in range(len(temp_list)-1):
                temp.append(temp_list[i]+temp_list[i+1])
            temp.append(temp_list[-1])
            list_result.append(temp)
            return list_result
		
		
		
		
		
		