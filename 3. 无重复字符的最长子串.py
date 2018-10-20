class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        list_str = list(s)
        long_list = []
        result_len = 0
        if len(list_str) == 0:
            return 0
        #动态规划解法（滑块法）
        for i in range(len(list_str)):
            if list_str[i] in long_list:
                long_list = long_list[(long_list.index(list_str[i])+1):]#从第出现重复字母的位置截断
                long_list.append(list_str[i])
            else:
                long_list.append(list_str[i])
                
            if len(long_list) > result_len:#记录最长的字符串
                result_len = len(long_list)
        return result_len