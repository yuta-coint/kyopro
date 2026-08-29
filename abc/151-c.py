N,M = map(int,input().split())
last=-1
cnt=0
t = 0
temp = []
for i in range(M):
    X,Y=map(int,input().split())
    if last==-1:
        if X==1 or X==2:
            t+=1
        if X==2:
            cnt+=1
        elif X>2:
            temp.append(X)
    elif last==Y:
            cnt+=1
    if i==M-1:
        if X==N-1 or X==N:
            t+=1
        if X==N-1:
            cnt+=1
        elif X<N-1:
            temp.append(N-X+1)
    last=Y
if t==1:
    print("Takahashi")
if t==2:
    if cnt&1:
        print("Takahashi")
    else:
        print("Aoki")
if t==0 and M!=0:
    if temp[0]==temp[1]:
        if cnt&1:
            print("Takahashi")
        else:
            print("Aoki")
    elif abs(temp[0]-temp[1])>=2:
        print("Takahashi")
    else:
        if cnt&1 and min(temp[0],temp[1])&1:
            print("Aoki")
        else:
            print("Takahashi")
if M==0:
    if N&1:
        print("Takahashi")
    else:
        print("Aoki")