def TwoStrComLength(str1,str2):
    str1_len = len(str1)
    str2_len = len(str2)
    matric = [[0]*str1_len for i in range(str2_len)]
    max_len = 0
    for i in range(str1_len):
        for j in range(str2_len):
            if str1[i] == str2[j]:
                if i != 0 and j != 0:
                    matric[i][j] = matric[i-1][j-1] + 1 #两字符串均不是起始字符
                else:
                    matric[i][j] = 1 #至少有字符串是起始字符串
            else:
                matric[i][j] = 0
            if matric[i][j] > max_len:
                max_len = matric[i][j]
    return max_len
	
str1 = "abcdefg"
str2 = "efgabcd"
TwoStrComLength(str1,str2)