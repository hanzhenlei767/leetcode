class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        rtn = []
        for i in nums:
            if i in rtn:
                rtn.remove(i)
            else:
                rtn.append(i)
        return rtn
        