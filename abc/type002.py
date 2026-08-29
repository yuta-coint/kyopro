import sys
sys.setrecursionlimit(10**6)
n = int(input())
def search(s,i):
    if i == n:
        cnt = 0
        for j in range(n):
            if s[j]=="(":
                cnt+=1
            else:
                cnt-=1
                if cnt<0:
                    break
        else:
            if cnt==0:
                print(s)
    else:
        search(s+"(",i+1)
        search(s+")",i+1)
search("",0)