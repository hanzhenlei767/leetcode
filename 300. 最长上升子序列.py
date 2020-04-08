'''
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4 
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
'''

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