import sys
input = sys.stdin.readline
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
    N,M = map(int,input().split())
    mat = [[0 for j in range(M)] for i in range(N)]
    for i in range(N):
        T = int(input())
        A = list(map(int,input().split()))
        for j in range(T):
            mat[i][A[j]-1]=1
    S = list(map(int,input().split()))
    mat,one_column,completed = Gaussian_elimination(mat,N,M)
    temp = [0 for j in range(M)]
    for i in range(completed):
        if S[one_column[i]]==1:
            for j in range(M):
                temp[j]^=mat[i][j]
    if S==temp:
        print(pow(2,N-completed,998244353))
    else:
        print(0)
main()