import sys
input = sys.stdin.readline
n = int(input())
limit = [0 for i in range(n)]
cnt = 0
under = 0
a1 = [[0,2,4],[0,2,3],[0,2,5],[1,3,5],[1,3,6],[1,4,6],[4,5,6]]
a2 = [[0,2,3],[0,2,4],[0,2,4],[1,5,6],[1,5,7],[1,5,7],[3,4,6],[3,6,7]]
a4 = [[4,5,7],[3,6,7],[3,4,5],[1,2,6],[0,6,7],[0,1,2],[8,9,10],[3,4,5],[8,9,10],[0,1,2],[8,9,10]]
a3 = [[4,5,6],[2,3,6],[0,5,6],[1,3,4],[0,1,2],[7,8,9],[3,4,5],[7,8,9],[0,1,2],[7,8,9]]
if n%6==1:
    for i in range(7):
        ans = ["." for i in range(n)]
        for j in range(3):
            ans[a1[i][j]]="#"
        print(*ans,sep="")
    cnt = 7
elif n%6==2:
    for i in range(8):
        ans = ["." for i in range(n)]
        for j in range(3):
            ans[a2[i][j]]="#"
        print(*ans,sep="")
    cnt = 8
elif n%6==3:
    for i in range(9):
        ans = ["." for i in range(n)]
        for j in range(3):
            ans[i//3]="#"
            ans[i//3+3]="#"
            ans[i//3+6]="#"
        print(*ans,sep="")
    cnt =9
elif n%6==4:
    for i in range(10):
        ans = ["." for i in range(n)]
        for j in range(3):
            ans[a3[i][j]]="#"
        print(*ans,sep="")
    cnt = 10
elif n%6==5:
    for i in range(11):
        ans = ["." for i in range(n)]
        for j in range(3):
            ans[a4[i][j]]="#"
        print(*ans,sep="")
    cnt = 11
else:
    cnt = 0
while cnt<n:
    ans = ["." for i in range(n)]
    for j in range(3):
        ans[cnt]="#"
        ans[cnt+2]="#"
        ans[cnt+4]="#"
    for i in range(3):
        print(*ans,sep="")
    ans = ["." for i in range(n)]
    for j in range(3):
        ans[cnt+1]="#"
        ans[cnt+3]="#"
        ans[cnt+5]="#"
    for i in range(3):
        print(*ans,sep="")
    cnt+=6
