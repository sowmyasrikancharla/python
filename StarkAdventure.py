#Mr Stark is facing the north. Peter is in trouble, and he is facing the south. Stark being his mentor will protect him as soon as he sees that Peter is in trouble.
# Stark's suit is programmed to rotate automatically in the direction of most enemies. By analyzing the direction in which most enemies are heading, the suit provides you with the next set of suit instructions in
# the form of a string S.
# When Stark faces south, he ignores the rest of his suit instructions and immediately goes to rescue Peter.
# Write a program that reads the set of suit instructions S and determines whether Stark will be able to save Peter.
# Note
# The string S contains either L or R. The letter L indicates left and the letter R indicates right
#Code
t=int(input())
directions=["North","East","South","West"]*10
for i in range(t):
    s=input()
    c=0
    ind=20
    for j in s:
        if(j=="R"):
            ind=ind+1
        else:
            ind=ind-1
        if(directions[ind]=="South"):
            c=1
    if c==1:
        print("YES")
    else:
        print("NO")
