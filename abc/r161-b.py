T = int(input())
for case in range(T):
    N=int(input())
    if N<7:
        print(-1)
        continue
    #最上位ビット
    top = 1<<(len(bin(N))-3)
    N-=top
    if N==0:
        print(top*7//8)
        continue
    middle = 1<<(len(bin(N))-3)
    N-=middle
    if N==0:
        if middle>=4:
            print(top+(middle*3//4))
        else:
            print(top*7//8)
        continue
    bottom = 1<<(len(bin(N))-3)
    print(top+middle+bottom)