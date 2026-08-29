import sys
input = sys.stdin.readline
def main():
    n=  int(input())
    a = list(map(int,input().split()))
    ans = 1<<60
    for i in range(n):
        temp = 0
        ma = 0
        for j in reversed(range(i)):
            time = ma//a[j]+1
            ma = a[j]*time
            temp+=time
        ma = 0
        for j in range(i+1,n):
            time = ma//a[j]+1
            ma = a[j]*time
            temp+=time
        ans = min(ans,temp)
    print(ans)
main()