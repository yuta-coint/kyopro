#基準値以上のものがK個以上あるようなもので、最大のもの？
from bisect import bisect_left
N,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
C.sort()
ok = 0
ng = 4*(10**18)
while ok+1<ng:
    norma = (ng+ok)//2
    score = 0
    for i in range(N):
        flag = 0
        for j in range(N):
            #欲しいC
            kijun = ((norma-A[i]*B[j]-1)//(A[i]+B[j]))+1
            atari = bisect_left(C,kijun)
            score += N-atari
            if score>=K or atari==N:
                break
            flag = 1
        #Aが弱すぎてこれ以上希望が持てない場合はそこでおわり
        if score>=K or flag == 0:
            break
    if score >=K:
        ok = norma
    else:
        ng = norma
print(ok)