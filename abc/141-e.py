#Z
n = int(input())
s = input()
#iスタートとjスタートの重複度を確かめよう
#leftから始まる文字列との重複度
def z_algo(left):
    z = [0 for i in range(n)]
    i = left+1
    j=0
    z[left] = n-left
    while i<n:
        #print(i)
        #jはleftとiから始まる文字列の重複度
        if i+j == n:
            z[i]=j
            i+=1
            j-=1
            continue
        while i+j<n and s[left+j]==s[i+j]:
            j+=1
            z[i] = j
        if j==0:
            i+=1
            continue
        for k in range(1,j):
            if k+z[left+k]<j:
                z[k+i]=z[left+k]
            else:
                i+=k
                j-=k
                break
        else:
            i+=j
            j=0
    return(z)
ans = 0
for i in range(n):
    zz = z_algo(i)
    for k in range(i,n):
        if k>=i+zz[k]:
            ans = max(ans,zz[k])
print(ans)

