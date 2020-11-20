'''
给定一个正整数数组 nums。

找出该数组内乘积小于 k 的连续的子数组的个数。

示例 1:

输入: nums = [10,5,2,6], k = 100
输出: 8
解释: 8个乘积小于100的子数组分别为: [10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6]。
需要注意的是 [10,5,2] 并不是乘积小于100的子数组。
说明:

0 < nums.length <= 50000
0 < nums[i] < 1000
0 <= k < 10^6
'''

'''
i，j都指向首元素。

s为乘积，s不断乘以num【j】得到子数组乘积，满足条件小于k时n+=（j-i+1），n是计数器。

首先我们考察这样一个事实。

假设k很大，有1000.

数组为【1,2,3,4,5】

那么任何子数组都是满足的，针对刚才的方法，n=1+2+3+4+5=15

正好对应所有长度的子数组，

但是不满足（乘积过大时将i向前移动并且除以num【i】以减小乘积这样又得到子数组的乘积小于k子数组）。

这样相当于解决了以num【i】开头的子数组满足条件的值，

接下来求以num【i+1】开头的。
'''

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k<=1:
            return 0
        n,i=0,0
        mul=1
        for j in range(len(nums)):
            mul*=nums[j]
            while mul>=k:
                mul//=nums[i]
                i+=1
            n+=(j-i+1)
        return n


class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n=0
        dp=[[1 for x in range(len(nums))] for y in range(len(nums))]
        for i in range(len(nums)):
            dp[i][i]=nums[i]
            if dp[i][i]<k:
                n+=1
        for j in range(1,len(nums)):
            i=0
            while i<len(nums) and j<len(nums):
                dp[i][j]=dp[i][j-1]*dp[i+1][j]//dp[i+1][j-1]
                if dp[i][j]<k:
                    n+=1
                i+=1
                j+=1
        return n