class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr_len = len(nums)
		if arr_len == 0:
			return None
		min_sum = [nums[0]]
		for i in nums[1:]:
			if min_sum[-1] < 0:
				min_sum.append(min_sum[-1]+i)
			else:
				min_sum.append(i)
		return min(min_sum)