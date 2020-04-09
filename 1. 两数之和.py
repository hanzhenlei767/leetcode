'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''

#哈希法-空间换时间

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

#不使用额外空间

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            dif = target - nums[i]    # 计算差值
            nums[i] = '#'
            if dif in nums:           # 查看差值是否在剩余数字中
                return [i, nums.index(dif)]
        return []

# 无序数组
# 数组中两数之和等于target则返回两个数
# 数组中不存在两数之和等于target则返回两个最接近target的数


def twoSum(nums, target):
    nums.sort()
    print(nums)
    left = 0
    right = len(nums)-1
    min_diff = float("inf")
    
    while left<right:
        if (nums[left] + nums[right])  == target:
            return nums[left],nums[right]
        elif (nums[left] + nums[right])  > target:
            if abs(nums[left] + nums[right] - target) < min_diff:
                min_diff = abs(nums[left] + nums[right] - target)
                last = nums[left],nums[right]
            right = right - 1
        else:
            if abs(nums[left] + nums[right] - target) < min_diff:
                min_diff = abs(nums[left] + nums[right] - target)
                last = nums[left],nums[right]
            left = left + 1
    return last