from math import floor,sqrt
A,B = map(int,input().split())
board = floor((A/(2*B))**(2/3))
if board==0:
    ans = A
else:
    rg1 = sqrt(board)
    rg2 = sqrt(board+1)
    ans = min(A/rg1 + B*(board-1),A/rg2 + B*board)
print(ans)