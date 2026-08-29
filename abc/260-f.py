def main():
    import sys
    input = sys.stdin.readline
    S,T,M = map(int,input().split())
    conn=[False for i in range(T*T)]
    temp=[0 for i in range(T*T)]
    G = [set() for i in range(S)]
    for i in range(M):
        u,v = map(int,input().split())
        G[u-1].add(v-1-S)
    ans = -1
    for i in range(S):
        for t in G[i]:
            for s in G[i]:
                if t>=s:
                    continue
                if conn[s*T+t]:
                    ans = [temp[s*T+t]+1,i+1,s+S+1,t+S+1]
                    break
                else:
                    conn[s*T+t]=True
                    temp[s*T+t]=i
            if ans!=-1:
                break
        if ans!=-1:
            break
    if ans==-1:
        print(ans)
    else:
        print(*ans)
main()

