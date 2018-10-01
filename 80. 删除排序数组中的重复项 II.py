class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        index = 1
        count = 1
        base = nums[0]
        
        for i in range(1,len(nums)): 
            if nums[i] > base:
                base = nums[i]
                nums[index] = nums[i]
                index += 1
                count = 1
            else:
                if count >= 2:
                    pass
                else:
                    nums[index] = nums[i]
                    index += 1
                    count += 1
        return index
                