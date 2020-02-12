'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true
'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s1 = ['(','[','{']
        s2 = [')',']','}']
        s3 = ['()','[]','{}']
        
        temp_s = []
        for i in s:
            if i in s1:
                temp_s.append(i)
            elif i in s2:
                if temp_s != []:
                    if (temp_s.pop()+i) in s3:
                        pass
                    else:
                        return False
                else:
                    return False
        if len(temp_s) != 0:
            return False
        return True