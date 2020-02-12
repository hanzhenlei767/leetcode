'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
'''

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