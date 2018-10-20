class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=[1]*len(nums)
        if len(nums)==0:
            return 0
        for i in range(1,len(nums)):#必须以nums[i]结尾的子序列
            for j in range(0,i):
                if(nums[i]>nums[j]):#动态规划：要想增加最大子序列长度，大于某个位置的值是前提
                    a[i]=max(a[i],a[j]+1)#那么至少要比小的长1，否则长度就是1
        return max(a)