class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones, twos = 0, 0
        for num in nums:
            ones = (ones^num) & ~twos
            twos = (twos^num) & ~ones

        return ones
		
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
		return (3*sum(set(nums)) - sum(nums))//2