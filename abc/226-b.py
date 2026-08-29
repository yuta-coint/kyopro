N = int(input())
s = [tuple(map(int,input().split())) for i in range(N)]
s =set(s)
print(len(s))