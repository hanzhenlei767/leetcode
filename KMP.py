#问题：有一个文本串S，和一个模式串P，现在要查找P在S中的位置

#暴力法
def KMP(s,p):
    s_len = len(s)
    p_len = len(p)
    if s_len < p_len:
        return -1
    for i in range(0,s_len-p_len+1):
        for j in range(p_len):
            if p[j] != s[i+j]:
                break
            else:
                if j == p_len-1:
                    return i
    return -1
	
	
#KMP算法（ Knuth-Morris-Pratt 字符串查找算法）
	
def KMP_algorithm(string, substring):
    '''
    KMP字符串匹配的主函数
    若存在字串返回字串在字符串中开始的位置下标，或者返回-1
    '''
    pnext = gen_pnext(substring)
    n = len(string)
    m = len(substring)
    i, j = 0, 0
    while (i<n) and (j<m):
        if (string[i]==substring[j]):
            i += 1
            j += 1
        elif (j!=0):
            j = pnext[j-1]
        else:
            i += 1
    if (j == m):
        return i-j
    else:
        return -1

def gen_pnext(substring):
    """
    构造临时数组pnext
    """
    index, m = 0, len(substring)
    pnext = [0]*m
    i = 1
    while i < m:
        if (substring[i] == substring[index]):
            pnext[i] = index + 1
            index += 1
            i += 1
        elif (index!=0):
            index = pnext[index-1]
        else:
            pnext[i] = 0
            i += 1
    return pnext

if __name__ == "__main__":
    string = 'abcxabcdabcdabcy'
    substring = 'abcdabcy'
    out = KMP_algorithm(string, substring)
    print(out)


























