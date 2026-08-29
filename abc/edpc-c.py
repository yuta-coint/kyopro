N = int(input())
mountain,ocean,homework = map(int,input().split())
for i in range(N-1):
    a,b,c = map(int,input().split())
    mountain,ocean,homework = max(ocean,homework)+a,max(mountain,homework)+b,max(mountain,ocean)+c
print(max(mountain,ocean,homework))