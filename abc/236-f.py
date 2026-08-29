n = int(input())
c = list(map(int,input().split()))
c = [[c[i-1],i] for i in range(1,2**n)]
c.sort()
#choiceの中から好きなように組み合わせる
done = set([0])
choice = set()
ans = 0
for i in range(2**n-1):
    #choiceとの一次独立性
    if c[i][1] in done:
        continue
    k = [c[i][1]^j for j in done]
    for j in k:
        done.add(j)
    choice.add(c[i][1])
    ans+=c[i][0]
    #print(choice)
print(ans)

