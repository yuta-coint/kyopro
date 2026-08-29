D = int(input())
ans = 10**24
from math import floor
for x in range(2*(10**6)):
    if D-x**2<0:
        score = score = abs(x**2-D)
        if score<ans:
            ans = score
        break
    y = floor((D-x**2)**(0.5))
    score = abs(x**2+y**2-D)
    if score<ans:
        ans = score
    y+=1
    score = abs(x**2+y**2-D)
    if score<ans:
        ans = score
print(ans)