#Yash is solving a matrix problem as part of his entrance exam preparation.
# In that matrix problem, there is a square matrix of size N x N. Yash needs to calculate the sum of the upper and lower triangular
# elements of the matrix. Help Yash solve the given matrix problem.
# Write a program that reads the NX N matrix and prints the sum of the upper and lower triangular elements.
# Note
# The upper triangle consists of elements on the anti- diagonal and above on it.
# The lower triangle consists of elements on the anti- diagonal and below it.
#Code
n=int(input())
u=n
b=n-1
max_sum=0
min_sum=0
for i in range(1,n+1):
    l=list(map(int,input().split()))
    l1=l[:u]
    max_sum=max_sum+sum(l1)
    u=u-1
    l2=l[b:]
    min_sum+=sum(l2)
    b=b-1
print(max_sum)
print(min_sum)