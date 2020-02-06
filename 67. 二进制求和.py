'''
给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"
'''
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a,b = list(a),list(b)
        flag = 0
        last = []
        while a != [] or b != []:
            t_a,t_b = 0,0
            if a != []:
                t_a = int(a.pop())
            if b != []:
                t_b = int(b.pop())
            t = t_a + t_b + flag

            if t == 0:
                flag = 0
                last.append('0')
            elif t == 1:
                flag = 0
                last.append('1')
            elif t == 2:
                flag = 1
                last.append("0")
            else:
                flag = 1
                last.append("1")

        if flag == 1:
            last.append("1")

        return "".join(last[::-1])

