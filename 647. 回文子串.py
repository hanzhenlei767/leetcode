'''
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。

示例 1:

输入: "abc"
输出: 3
解释: 三个回文子串: "a", "b", "c".
示例 2:

输入: "aaa"
输出: 6
说明: 6个回文子串: "a", "a", "a", "aa", "aa", "aaa".
注意:

输入的字符串长度不会超过1000。
'''

class Solution:
    
    count = 0
    

    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(len(s)):
            left = i
            right = i
            while (left>=0) & (right<len(s)):
                if (s[left] == s[right]):
                    count = count + 1
                    left = left - 1
                    right = right + 1
                else:
                    break
                
            left = i
            right = i + 1
            while (left>=0) & (right<len(s) ):
                if (s[left] == s[right]):
                    count = count + 1
                    left = left - 1
                    right = right + 1
                else:
                    break
            
        return count
    
    
        
        
        