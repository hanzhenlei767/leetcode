'''
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 num1 成为一个有序数组。

 

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
 

示例:

输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]
'''



class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        last_list = []
        m_head = 0
        n_head = 0
        while (m!=m_head) & (n!=n_head):
            if nums1[m_head] >= nums2[n_head]:
                last_list.append(nums2[n_head])
                n_head += 1
            else:
                last_list.append(nums1[m_head])
                m_head += 1
        if m == m_head:
            last_list = last_list + nums2[n_head:]
        else:
            last_list = last_list + nums1[m_head:m]
        for i in range(len(last_list)):
            nums1[i] = last_list[i]