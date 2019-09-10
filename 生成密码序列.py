
# coding: utf-8

#生成密码序列
#arr:观测序列
#key:连续key个数之和
#arr_len:数组长度

def funtion(arr,key,arr_len):
    index = 0
    last = []
    for i in range(arr_len):#总密码数
        temp = 0
        index = i
        for _ in range(abs(key)):#生成密码累计加多少次
            if key > 0:
                index -= 1
                if index < 0:
                    index = arr_len -1
                temp += arr[index]
            else:
                index += 1
                if index == arr_len:
                    index = 0
                temp += arr[index]
        last.append(temp)
    return last
        

