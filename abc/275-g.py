N = int(input())
goods = [tuple(map(int,input().split())) for i in range(N)]
ng = 0
ok = 10
for _ in range(60):
    X = (ok + ng)/2
    low = 0
    up = 1
    death = False
    for i in range(N):
        A,B,C = goods[i]
        AX = A*X
        BX = B*X
        if AX >= C and BX >= C:
            continue
        elif AX <= C and BX <= C:
            death = True
            break
        elif AX >= C and BX <= C:
            tmp = (AX - C)/(AX - BX)
            if tmp < up:
                up = tmp
        elif AX <= C and BX >= C:
            tmp = (-AX + C)/(BX - AX)
            if tmp > low:
                low = tmp
        if low > up:
            death = True
            break
    if death:
        ng = X
    else:
        ok = X
print(ok)
    
