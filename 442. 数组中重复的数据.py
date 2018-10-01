class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hash_list = {}
        last_list = []
        for i in range(len(nums)):
            if nums[i] in hash_list:
                last_list.append(nums[i])
            else:
                hash_list[nums[i]] = 1
        return last_list