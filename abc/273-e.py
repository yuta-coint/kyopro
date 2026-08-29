def main():
    import sys
    input = sys.stdin.readline
    Q = int(input())
    saves = {}
    A = []
    temp = -1
    la = 0
    ans = []
    for i in range(Q):
        query = list(input().split())
        if query[0]=="ADD":
            A.append((query[1],temp))
            temp = la
            la+=1
        if query[0]=="DELETE":
            if temp>=0:
                temp = A[temp][1]
        if query[0]=="SAVE":
            saves[query[1]]=temp
        if query[0]=="LOAD":
            #空っぽだったらどうするか考えんと
            if query[1] in saves:
                temp=saves[query[1]]
            else:
                temp=-1
        #print(A)
        #print(temp)
        if temp == -1:
            ans.append(-1)
        else:
            ans.append(int(A[temp][0]))
    print(*ans)
main()
    
