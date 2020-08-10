'''
题目描述:
给定一个数组 nums 和一个目标值 k，找到和等于 k 的最长子数组长度。如果不存在任意一个符合要求的子数组，则返回 0。

注意:

nums 数组的总和是一定在 32 位有符号整数范围之内的。

示例:
示例 1:

输入: nums = [1, -1, 5, -2, 3], k = 3
输出: 4 
解释: 子数组 [1, -1, 5, -2] 和等于 3，且长度最长。
示例 2:

输入: nums = [-2, -1, 2, 1], k = 1
输出: 2 
解释: 子数组 [-1, 2] 和等于 1，且长度最长。
进阶:

你能使时间复杂度在 O(n) 内完成此题吗?
'''
#前缀和
class Solution:
    def maxSubArrayLen(self, nums, k):
        lookup = {0: -1}
        cur = 0
        res = 0
        for idx, val in enumerate(nums):
            cur += val
            if cur - k in lookup:
                res = max(res, idx - lookup[cur - k])
                
            # 记录前面和的最小位置，所以说存在数值就不改变
            if cur not in lookup:
                lookup[cur] = idx
        return res


#暴力法
def solution(a,k):
    #用于记录当前最大值
    tmp = 0
    #步长i从1到len(a)+1
    for i in range(1,len(a)+1):
        #j:表示窗口左端
        for j in range(len(a)-i+1):            
            #如果当前窗口的和为k，则当前最大值就是tmp和步长得最大值
            if sum(a[j:j+i]) == k:
                tmp = max(tmp,i)                
    return tmp






