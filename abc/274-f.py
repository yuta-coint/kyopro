def main():
    import sys
    input = sys.stdin.readline
    N,A = map(int,input().split())
    W = []
    X = []
    V = []
    for i in range(N):
        w,x,v = map(int,input().split())
        W.append(w)
        X.append(x)
        V.append(v)
    # N: 処理する区間の長さ
    ans = 0
    for i in range(N):
        candt = []
        temp = 0
        for j in range(N):
            if X[i]<=X[j]<=X[i]+A:
                temp+=W[j]
            if i==j:
                continue
            if V[i]==V[j]:
                continue
            #0では入っているけどすぐ外に出るパターン
            if (X[i]-X[j])/(V[j]-V[i])>=0 and V[i]>V[j]:
                candt.append(((X[i]-X[j])/(V[j]-V[i]),W[j]))
            if (X[i]-X[j])/(V[j]-V[i])>0 and V[i]<V[j]:
                candt.append(((X[i]-X[j])/(V[j]-V[i]),-W[j]))
            if (X[i]-X[j]+A)/(V[j]-V[i])>=0 and V[i]<V[j]:
                candt.append(((X[i]-X[j]+A)/(V[j]-V[i]),W[j]))
            if (X[i]-X[j]+A)/(V[j]-V[i])>0 and V[i]>V[j]:
                candt.append(((X[i]-X[j]+A)/(V[j]-V[i]),-W[j]))
        #print(candt)
        candt.sort()
        if temp>ans:
            ans=temp
        for i in range(len(candt)):
            temp -= candt[i][1]
            if temp>ans:
                ans=temp
    print(ans)
main()