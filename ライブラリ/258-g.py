#64bit整数であれば、1になっているbitの数を求めることができる！
def popcount(n):
  c=(n&0x5555555555555555)+((n>>1)&0x5555555555555555)
  c=(c&0x3333333333333333)+((c>>2)&0x3333333333333333)
  c=(c&0x0f0f0f0f0f0f0f0f)+((c>>4)&0x0f0f0f0f0f0f0f0f)
  c=(c&0x00ff00ff00ff00ff)+((c>>8)&0x00ff00ff00ff00ff)
  c=(c&0x0000ffff0000ffff)+((c>>16)&0x0000ffff0000ffff)
  c=(c&0x00000000ffffffff)+((c>>32)&0x00000000ffffffff)
  return c
def main():
    N = int(input())
    A = [list(input()) for i in range(N)]
    bitsetA = [[] for i in range(N)]
    cnt = 0
    dim = 0
    for i in range(N):
        for j in range(N):
            if A[i][j]=="1":
                cnt+=(1<<dim)
            dim+=1
            if j%60==59:
                bitsetA[i].append(cnt)
                cnt=0
                dim=0
        bitsetA[i].append(cnt)
        cnt=0
        dim=0
    lenbit = len(bitsetA[0])
    ans = 0
    #print(bitsetA)
    for i in range(N-1):
        for j in range(i+1,N):
            if A[i][j]=="0":
                continue
            for k in range(lenbit):
                ans+=popcount(bitsetA[i][k]&bitsetA[j][k])
    print(ans//3)
main()