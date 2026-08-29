a,b,d = map(int,input().split())
from math import sin,cos,radians
print(a*cos(radians(d))-b*sin(radians(d)),a*sin(radians(d))+b*cos(radians(d)))