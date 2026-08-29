import sys
input = sys.stdin.readline
#行簡約化後の行列、頭の1がある列、0でない列の数を返す。
def Gaussian_elimination(mat,N,M):
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
#計算量は|A|*|basis|
def xor_basis(A):
    basis = []
    for i in range(len(A)):
        e = A[i]
        for b in basis:
            if e^b <e:
                e = e^b
        if e>0:
            basis.append(e)
    #要らない1を消す。
    basis.sort(reverse=True)
    for i in range(len(basis)):
        for j in range(i):
            if basis[i]^basis[j] < basis[j]:
                basis[j]=basis[i]^basis[j]
    return(basis)
            
N,L,R = map(int,input().split())
A = list(map(int,input().split()))
sb=xor_basis(A)
sb.sort()
ans = []
keta = len(sb)
for num in range(L-1,R):
    temp = 0
    for i in range(keta):
        if (num>>i)&1:
            temp^=sb[i]
    ans.append(temp)
print(*ans)