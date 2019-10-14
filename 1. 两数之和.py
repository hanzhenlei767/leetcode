class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sub = {}
        for i in range(len(nums)):
            if nums[i] in sub:
                return [sub[nums[i]],i]
            else:
                sub[target - nums[i]] = i