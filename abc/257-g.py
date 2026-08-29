import typing
def z_algorithm(s: typing.Union[str, typing.List[int]]) -> typing.List[int]:
    '''
    Z algorithm
    Reference:
    D. Gusfield,
    Algorithms on Strings, Trees, and Sequences: Computer Science and
    Computational Biology
    '''

    if isinstance(s, str):
        s = [ord(c) for c in s]

    n = len(s)
    if n == 0:
        return []

    z = [0] * n
    j = 0
    for i in range(1, n):
        z[i] = 0 if j + z[j] <= i else min(j + z[j] - i, z[i - j])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if j + z[j] < i + z[i]:
            j = i
    z[0] = n

    return z
S = input()
T = input()
Z = z_algorithm(S+T)
Z = Z[len(S):]
LS = len(S)
LT = len(T)
for i in range(LT):
    Z[i]=min([Z[i],LS,LT-i])
#print(Z)
#i個連結でどこまでいけるか
m = [0 for i in range(LT+1)]
cnt = 0
for i in range(LT):
    #一個足すだけじゃ別に回っちゃうんか…反省
    while i>m[cnt]:
        if cnt==LT:
            break
        cnt+=1
    if cnt==LT:
        break
    m[cnt+1]=max(m[cnt+1],i+Z[i])
ans = -1
#print(m)
for i in range(LT+1):
    if m[i]>=LT:
        ans = i
        break
print(ans)