N,A1,A2,A3 = map(int,input().split())
mod = 998244353
N +=1
#未満に言い換え
b = len(bin(N))-2
ans = [[0 for i in range(A1*A2*A3)]]
ans[0][0]=1
for i in range(b):
    temp = [0 for i in range(A1*A2*A3)]
    for xyz in range(A1*A2*A3):
        x = xyz//(A2*A3)
        y = (xyz%(A2*A3))//A3
        z = xyz%A3
        temp[((x+(1<<i)%A1)%A1)*A2*A3+((y+(1<<i)%A2)%A2)*A3+(z+(1<<i)%A3)%A3]+=ans[-1][xyz]
        temp[((x+(1<<i)%A1)%A1)*A2*A3+((y+(1<<i)%A2)%A2)*A3+(z+(1<<i)%A3)%A3]%=mod
    ans.append(temp)
#一桁ずつ壊していく
t = 1<<b
pr = ans[b][0]
for i in reversed(range(b-1)):
    if (t>>i)&1:
        pass
    else:
        continue
    #A1に全ての桁を回収させる。
    