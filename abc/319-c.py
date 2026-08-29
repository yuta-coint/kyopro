c = [list(map(int,input().split())) for i in range(3)]
from itertools import permutations
cnt = 0
line = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
for r in permutations(range(9),9):
    flag = 0
    chk = [-1*(i+1) for i in range(9)]
    for i in r:
        chk[i]=c[i//3][i%3]  
        for l in line:
            s,t,u = chk[l[0]],chk[l[1]],chk[l[2]]
            if s>=0 and t>=0 and u>=0:
                continue
            if s==t or s==u or t==u:
                cnt+=1
                flag = 1
                break
        if flag==1:
            break
print(1-cnt/362880)