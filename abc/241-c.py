import sys
input = sys.stdin.readline
n = int(input())
s = [input() for i in range(n)]
ans = "No"
for i in range(n-5):
    for j in range(n-5):
        chkb = 0
        chkw = 0
        for t in range(6):
            if s[i+t][j+t]=="#":
                chkb+=1
            if s[i+t][j+5-t]=="#":
                chkw+=1
        if chkb>=4 or chkw>=4:
            ans = "Yes"
for i in range(n):
    for j in range(n-5):
        chka = 0
        chks = 0
        for t in range(6):
            if s[i][j+t]=="#":
                chka += 1
            if s[j+t][i]=="#":
                chks +=1
        if chka>=4 or chks>=4:
            ans = "Yes"
print(ans)

