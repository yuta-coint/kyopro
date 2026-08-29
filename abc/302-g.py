N = int(input())
A = list(map(int,input().split()))
count1 = A.count(1)
count2 = A.count(2)
count3 = A.count(3)
count4 = A.count(4)
A1 = A[:count1]
A2 = A[count1:count1+count2]
A3 = A[count1+count2:count1+count2+count3]
A4 = A[count1+count2+count3:]
####以下全部嘘
stock1 = []
ans = 0
for i in A1:
    if i!=1:
        stock1.append(i)
        ans+=1
stock1.sort(reverse=True)
for i in A2:
    if i==1:
        i = stock1.pop()
stock2 = []
for i in A2:
    if i>2:
        stock2.append(i)
        ans+=1
stock2.sort(reverse=True)
for i in A3:
    if i==1:
        i=stock1.pop()
    if i==2:
        i=stock2.pop()
for i in A3:
    if i==4:
        ans+=1
print(ans)