#https://atcoder.jp/contests/abc353/submissions/53377473
temp = [(0,-1) for i in range(4*(10**5))]
N = int(input())
S = list(input().split())
S.sort()
#print(S)
end = len(S[0])
for t in range(len(S[0])):
    temp[t]=(1,0)
ans = 0
for i in range(1,N):
    #print(temp[:5],ans)
    for t in range(min(end,len(S[i]))):
        if S[i-1][t]==S[i][t]:
            if temp[t][1]==i-1:
                temp[t]=(temp[t][0]+1,i)
            else:
                ans+=temp[t][0]*(temp[t][0]-1)//2
                temp[t]=(1,i)
        else:
            end=t
            break
    for t in range(min(end,len(S[i])),len(S[i])):
        ans+=temp[t][0]*(temp[t][0]-1)//2
        temp[t]=(1,i)
    end = len(S[i])
#print(temp[:5],ans)
for t in range(4*(10**5)):
    ans+=temp[t][0]*(temp[t][0]-1)//2
print(ans)