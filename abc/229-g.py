s = input()
k=int(input())
n = len(s)
ly = []
for i in range(n):
    if s[i]=="Y":
        ly.append(i)
sumy = [0]
sy = 0
for i in ly:
    sy+=i
    sumy.append(sy)
M=len(ly)+1
m=0
while M>m+1:
    temp = (m+M)//2
    for i in range(len(ly)+1-temp):
        i3 = i+temp-1
        i2 = (i+i3)//2
        cost = 0
        w = temp//2
        cost = sumy[i3+1]-sumy[i2+1]+sumy[i]-sumy[i2]
        if temp%2==1:
            cost-=w*(w+1)
        else:
            cost-=w*w+ly[i2]
        if cost<=k:
            m=temp
            break
    else:
        M=temp
print(m)
