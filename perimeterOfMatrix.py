#Problem Statement: Write a program that reads an M x N matrix and prints the perimeter of the matrix.
#Note
#The perimeter of the matrix is defined as the sum of all the elements on the four edges of the matrix.
#Input
#The first line of input contains space-separated integers representing M and N respectively.
#The next M lines of input contain N space-separated integers representing the matrix.
#Code
a=input().split()
m=int(a[0])
n=int(a[1])
s=0
mat=[]
c=0
for i in range (1,m+1):
    b=input().split()
    for j in b:
        mat.append(int(j))
matrix=[]
for i in range(1,m+1):
    for j in range(1,n+1):
        matrix.append(mat[c])
        if(i==1 or i==m or j==1 or j==n):
            s=s+mat[c]
        c=c+1
print(s)