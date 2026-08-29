import sys
input = sys.stdin.readline
n = int(input())
users = set()
for i in range(1,n+1):
    s = input()
    if s not in users:
        print(i)
        users.add(s)