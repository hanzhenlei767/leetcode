'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
'''

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        if nums_len == 0:
            return None
        max_sum = float("-inf")
        cur_sum = 0
        for i in range(0,nums_len):
            if cur_sum <= 0:
                cur_sum = nums[i]
            else:
                cur_sum += nums[i]
            if cur_sum>max_sum:
                max_sum = cur_sum
        return max_sum