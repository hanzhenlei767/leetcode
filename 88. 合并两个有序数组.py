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