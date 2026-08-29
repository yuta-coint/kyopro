H,M = map(int,input().split())
def misjudge(h,m):
    new_h = h-(h%10)+(m//10)
    new_m = (h%10)*10+m%10
    if 0<=new_h<24 and 0<=new_m < 60:
        return(True)
    else:
        return(False)
while True:
    if misjudge(H,M):
        break
    if M==59:
        M=0
        H+=1
        H%=24
    else:
        M+=1
print(H,M)
