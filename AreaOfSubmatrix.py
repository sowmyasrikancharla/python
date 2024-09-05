# Problem Statement: You are given an M x N matrix and a number K. In the given M x N matrix, you need to delete K rows from both the top and the bottom and delete K columns from both the left and the right.
#  Finally, calculate the product of all elements in the resulting matrix.
#Write a program that reads an M x N matrix and a number K and prints the product of all elements in the resulting matrix.
# Code
n=list(input().split())
rows=int(n[0])
cols=int(n[1])
matrix=[]
for i in range(rows):
    l=list(map(int,input().split()))
    matrix.append(l)
k=int(input())
start_row=0+k
end_row=rows-k
start_col=0+k
end_col=cols-k
result=1
mat1=[]
for i in range(start_row,end_row):
    for j in range(start_col,end_col):
        mat1.append(matrix[i][j])
if(mat1==[]):
    print(0)
else:
    for i in mat1:
        result*=i
    print(result)

