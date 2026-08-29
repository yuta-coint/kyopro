def main():
    N = int(input())
    S = list(input())
    flag = 0
    for i in range(N):
        if S[i]=="p":
            S[i]=1
        else:
            S[i]=0
    for i in range(N):
        if S[i]==1:
            L=i
            break
    else:
        temp = S
        flag = 1
    #print(S)
    if flag ==0:
        temp = [float("inf")]
        for i in range(L,N):
            if S[i]==1:
                t = S[L:i+1]
                t.reverse()
                #print(t)
                for j in range(len(t)):
                    t[j] = 1-t[j]
                #print(t)
                t = S[:L]+t+S[i+1:]
                if t<temp:
                    temp = t
    for i in range(N):
        if temp[i]==0:
            temp[i]="d"
        else:
            temp[i]="p"
    print(*temp,sep="")
main()