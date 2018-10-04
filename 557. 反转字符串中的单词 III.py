class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        list_s = []
        for i in s.split(" "):
            list_s.append(i[::-1])
        return " ".join(list_s)