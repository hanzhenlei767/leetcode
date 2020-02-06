'''
给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。

如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指仅由字母组成、不包含任何空格的 最大子字符串

'''


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(s.strip())
        if s == []:
            return 0
        count = 0
        while True:
            if s != []:
                temp = s.pop()
                if temp != " ":
                    count += 1
                else:
                    return count
            else:
                return count