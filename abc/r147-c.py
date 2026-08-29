import sys
input = sys.stdin.readline
N = int(input())
lr = []
L = []
R = []
t = []
for i in range(N):
    l,r = map(int,input().split())
    lr.append((l,r))
    L.append(l)
    R.append(r)
L.sort()
R.sort()
Rscore = [0]
for i in range(N):
    Rscore.append(Rscore[-1]+R[i]*(-N+1+2*i))
Lscore = [0]
for i in reversed(range(N)):
    Lscore.append(Lscore[-1]+L[i]*(-N+1+2*i))
ans = float("inf")
k=N
#print(Lscore)
#print(Rscore)
for i in range(N//2+1):
    #print(k,i)
    if k>0:
        while L[N-k]<R[i]:
            k-=1
            if k==0:
                break
    if k>(N//2):
        continue
    ans = min(ans,Rscore[i]+(N-k-i)*(i-k)*R[i]+Lscore[k])
    #print(Rscore[i]+(N-k-i)*(i-k)*R[i]+Lscore[k],Rscore[i],(N-k-i)*(i-k),Lscore[k])
k=0
for i in range(N):
    if k<N:
        while L[i]>R[k]:     
            k+=1
            if k==N:
                break 
    if k>(N//2) or (N-i-1)>(N//2):
        continue
    ans = min(ans,Rscore[k]+(i+1-k)*(k+i+1-N)*L[i]+Lscore[N-1-i])
    #print(i,k,Rscore[k]+(i+1-k)*(k+i+1-N)*L[i]+Lscore[N-1-i],Rscore[k],(i+1-k)*(k+i+1-N)*L[i],Lscore[N-1-i])
print(ans)