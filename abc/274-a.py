A,B = map(int,input().split())
from math import floor
ave = floor(((B*1000)/A)+0.5)/1000
print('{:.3f}'.format(ave))