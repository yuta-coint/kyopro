n,k = map(int,input().split())
a = list(map(int,input().split()))
ma = 3*(10**9)
mi = -1
#m以上全部乗る
while ma>mi+1:
    m = (ma+mi)//2
    ride = 0
    for i in range(n):
        if a[i]>=m:
            ride+=a[i]-m+1
    if ride <=k:
        ma=m
    else:
        mi=m
ride = 0
enjoy = 0
for i in range(n):
    if a[i]>=ma:
        ride+=a[i]-ma+1
        enjoy+=(a[i]+ma)*(a[i]-ma+1)//2
if ma>=1:
    enjoy += (k-ride)*(ma-1)
print(enjoy)
    
