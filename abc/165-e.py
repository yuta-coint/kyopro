N,M = map(int,input().split())
temp = N//2
temp2 = 1
for i in range(1,M+1):
    if i&1:
        print(temp+1,temp+i+1)
        temp-=1
    else:
        print(temp2+1,(temp2-i)%N+1)
        temp2+=1