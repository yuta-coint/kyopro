P = [0, 11, 31, 34, 32, 2, 3, 29, 27, 10, 4, 21, 9, 12, 28, 22, 36, 18, 30, 16, 19, 26, 24, 13, 35, 15, 17, 7, 37, 5, 8, 23, 14, 20, 33, 1, 6, 25]
import random
def pr1(i,j,k):
    if P[i]+P[j]>P[k]:
        return("Yes")
    else:
        return("No")
import sys
def pr(aa,ii,uu):
    if aa==uu or ii==uu:
        return("Yes")
    else:
        print("?",aa,ii,uu)
        sys.stdout.flush()
        return(input())
N = int(input())
#P = [0] + random.shuffle([i for i in range(1,N)])
if N == 1:
    print("!",1)
    exit()
#１の特定と大きさによるグループ分けのフェイズ
ans = [0 for i in range(N+1)]
rank = [-1 for i in range(N+1)]
box=[1,2,0]
for i in range(3,N+1):
    for b in range(3):
        if box[b]==0:
            box[b]=i
    f,g,h = box[0],box[1],box[2]
    s = pr(f,g,h)
    t = pr(h,g,f)
    if s=="No":
        box[2]=0
    elif t=="No":
        box[0]=0
    else:
        box[1]=0
box.remove(0)
if pr(box[0],box[0],box[1])=="Yes":
    y = box[1]
else:
    y = box[0]
ans[y]=1
order = []
ll  = 0
for i in range(1,N+1):
    if i==y:
        continue
    m = 0
    M = ll+1
    while m+1<M:
        t = (m+M)//2
        s = pr(order[t-1],y,i)
        #s = test(order[t-1],y,i)
        if s=="Yes":
            M=t
        else:
            m=t
    order.insert(m,i)
    ll+=1
for i in range(N-1):
    ans[order[i]]=i+2
print("!",*ans[1:])