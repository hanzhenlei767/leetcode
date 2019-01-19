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