
# coding: utf-8

#矩阵循环打印

def function(mat,row,col,r_index,c_index):
    a = (row-r_index+1)//2
    b = (row-r_index+1)%2
    c = (col-c_index+1)//2
    d = (col-c_index+1)%2
    
    for _ in range(min((a+b),(c+d))):
        for i in range(col-c_index+1):
            print(mat[r_index-1][c_index-1+i])
        print("-------------")
        for i in range(row-r_index):
            print(mat[r_index+i][col-1])
        print("-------------")
        for i in range(col-c_index):
            if row != r_index:
                print(mat[row-1][col-2-i])
        print("-------------")
        for i in range(row-r_index-1):
            print(mat[row-2-i][c_index-1])
        print("-------------")
        row = row - 1
        col = col - 1
        r_index = r_index + 1
        c_index = c_index + 1

mat = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]
function(mat,4,5,4,5)