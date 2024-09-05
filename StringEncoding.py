# ryan has two strings S and T containing lowercase alphabets. His student Ram has been asked to encode the string in the following manner.

# Ram should think a positive number K that may transform S into T by shifting each character of S to the right of K positions.

# If K = 2 then a is shifted to the right of 2 positions, it will become C.

# If K3 then x is shifted to the right of 3 positions, it will become

# a.
#Code
s=input()
t=input()
s_list=[]
t_list=[]
res=[]
c=0
for i in s:
    s_list.append(ord(i))
for i in t:
    t_list.append(ord(i))
if(len(s_list)!=len(t_list)):
    print("No")
else:
    for i in range(len(s_list)):
        if(t_list[i]-s_list[i]<0):
            res.append(26+(t_list[i]-s_list[i]))
        else:    
            res.append(t_list[i]-s_list[i])
if(c==0):
    st=res[0]
    if(res.count(st)==len(res)):
        print("Yes")
    else:
        print("No")
else:
    print("No")