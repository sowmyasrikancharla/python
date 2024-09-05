#Write a program that reads an Nx N matrix and checks if it is a unique matrix or not.
#A Unique Matrix is a matrix in which every row and column contains all integers from 1 to N.
#Input
#The first line of input contains an integer representing N.
#The next N lines of input contain N space-separated integers representing the matrix.
#Code
def check_count(l,n):
    l2=[]
    for i in l:
        if(i>0 and i<=n):
            l2.append(l.count(i))
        else:
            l2.append(0)
    if(l2==[1]*n):
        return 1
    else:
        return 0

n=int(input())
check_list=[]
main_list=[]
trans=[]
for i in range(1,n+1):
    l=list(map(int,input().split()))
    main_list.append(l)
    check_list.append(check_count(l,n))
for i in range(n):
    trans.append([0]*n)
for i in range(len(main_list)):
    for j in range(len(main_list[0])):
        trans[i][j]=main_list[j][i]
    l=trans[i][:]
    check_list.append(check_count(l,n))
if (0 in check_list):
    print("False")
else:
    print("True")