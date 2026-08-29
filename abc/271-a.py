sixteen = "0123456789ABCDEF"
N = int(input())
ans =  sixteen[N//16]+sixteen[N%16]
print(ans)