def Gaussian_elimination(mat,N,M):
    #N行M列の行列matに掃き出し法を施し、
    #変形後の行列、1が出ている列の一覧,1が一つだけある列の数を返す
    completed = 0
    one_column = []
    for j in range(M):
        all_zero = True
        #全ゼロだったら掃きださなくて楽なのにな
        for i in range(completed,N):
            if mat[i][j]==1:
                all_zero=False
                top = i
                break
        if all_zero:
            continue
        #1を引っ張り上げる
        mat[completed],mat[top]=mat[top],mat[completed]
        one_column.append(j)
        #1を全消し!!
        for i in range(N):
            if i==completed:
                continue
            if mat[i][j]==1:
                for t in range(M):
                    mat[i][t]^=mat[completed][t]
        completed+=1
        if completed==N:
            break
    return(mat,one_column,completed)
def main():
    N = int(input())
    A = list(map(int,input().split()))
    s = 0
    for i in range(N):
        s^=A[i]
    bits = []
    red_blue =  [[] for  i in range(N)]
    ans = 0
    for j in reversed(range(60)):
        if (s>>j)&1:
            ans+=(1<<j)
        else:
            bits.append(j)
            temp = []
            for i in range(N):
                red_blue[i].append((A[i]>>j)&1)
    m,oc,c = Gaussian_elimination(red_blue,N,len(bits))
    for j in range(len(bits)):
        temp = 0
        for i in range(N):
            temp^=m[i][j]
        ans+=2*temp*(1<<bits[j])
    print(ans)
main()