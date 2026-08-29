T =int(input())
for _ in range(T):
    A,B,C = map(int,input().split())
    cand = [A,C,(A+B+C)//3]
    print(min(cand))