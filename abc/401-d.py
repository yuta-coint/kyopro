N,K = map(int,input().split())
S = list(input())
for i in range(N-1):
    if S[i]=="o":
        S[i+1]="."
    if S[i+1]=="o":
        S[i] = "."
#〇がもともとちょうどK個なら全部.にしなきゃいけない。
K_min = 0
for i in range(N):
    if S[i]=="o":
        K_min+=1
if K_min == K:
    for i in range(N):
        if S[i]=="?":
            S[i]="."
    print(*S,sep="")
    exit()
#連結成分をカウントして、最大で何文字入るかを考える。
#偶数の連結成分なら、何も潰れない
#奇数の連結成分なら、片方潰れる
K_max = K_min
cnt = 0
jiyu = []
while cnt<N:
    if S[cnt]!="?":
        cnt+=1
        continue
    temp = 0
    while S[cnt]=="?":
        cnt+=1
        temp+=1
        if cnt == N:
            break
    K_max+=(temp+1)//2
    jiyu.append((cnt-temp,temp))
if K_max>K:
    print(*S,sep="")
else:
    for s,t in jiyu:
        if t&1:
            for i in range(t):
                if i&1:
                    S[s+i]="."
                else:
                    S[s+i]="o"
    print(*S,sep="")
