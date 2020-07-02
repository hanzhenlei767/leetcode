'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
示例 3:

输入: [1,3,5,6], 7
输出: 4
示例 4:

输入: [1,3,5,6], 0
输出: 0
'''

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums)-1            # 初始化左右端点位置
        while left <= right:                    # 当条件合法时
            mid = (right + left) // 2           # 获取中点，如果是偶数取靠左的位置
            if nums[mid] == target:             # 找到该数
                return mid                      # 直接返回
            elif nums[mid] > target:            # 如果当前位置数比插入值大
                right = mid - 1                 # 更新右端点
            else:                               # 如果当前位置数比插入值小
                left = mid + 1                  # 更新左端点
        return left                             # 返回插入位置，这里是左端位置