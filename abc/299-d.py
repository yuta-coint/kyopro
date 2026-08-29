N= int(input())
m = 1
M = N
import sys
while m+1<M:
    temp = (m+M)//2
    print("?",temp)
    sys.stdout.flush()
    S=int(input())
    if S==1:
        M = temp
    else:
        m = temp
print("!",m)