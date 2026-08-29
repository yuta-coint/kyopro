import math
import sys
input = sys.stdin.readline
t = int(input())
L,X,Y = map(int,input().split())
q = int(input())
for i in range(q):
    e = int(input())
    s = math.pi*2*e/t
    y = -math.sin(s)
    z = 1-math.cos(s)
    y*=L/2
    z*=L/2
    #print(math.sqrt((z*z)/(X**2+(Y-y)**2)))
    print(math.atan(math.sqrt((z*z)/(X**2+(Y-y)**2)))*180/math.pi)
