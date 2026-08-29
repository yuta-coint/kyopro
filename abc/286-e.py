v = int(input())
A = list(map(int,input().split()))
S = [input() for i in range(v)]
big = 10**13
length = [["INF" for i in range(v)] for j in range(v)]
for i in range(v):
    length[i][i]=0
for i in range(v):
    for j in range(v):
        if S[i][j]=="Y":
            length[i][j] = big-A[i]
for i in range(v):
     for j in range(v):
         for k in range(v):
             if length[j][i]!="INF" and length[i][k]!="INF":
                 if length[j][k] == "INF":
                     length[j][k]=length[j][i]+length[i][k]
                 elif length[j][k]>length[j][i]+length[i][k]:
                     length[j][k]=length[j][i]+length[i][k]
Q = int(input())
for i in range(Q):
    u,v = map(int,input().split())
    u,v = u-1,v-1
    #print(length[u][v])
    if length[u][v]=="INF":
        print("Impossible")
        continue
    ans1 = ((length[u][v]-A[v]-1)//big)+1
    ans2 = ans1*big-length[u][v]+A[v]
    print(ans1,ans2)

