def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    champ = {}
    score = {}
    iso = {}
    for i in range(N):
        m = int(input())
        for _ in range(m):
            p,e = map(int,input().split())
            if p in champ:
                if e>score[p]:
                    champ[p]=i
                    score[p]=e
                    iso[p]=True
                elif e==score[p]:
                    iso[p]=False
            else:
                champ[p]=i
                score[p]=e
                iso[p]=True
    chk = [False for i in range(N)]
    for i in iso:
        if iso[i]:
            chk[champ[i]]=True
    ans = 0
    for i in range(N):
        if chk[i]:
            ans+=1
    if ans!=N:
        ans+=1
    print(ans)
main()