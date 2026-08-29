time = 21
K=int(input())
time+=K//60
minutes=str(K%60)
minutes = minutes.zfill(2)
print(str(time)+":"+minutes)