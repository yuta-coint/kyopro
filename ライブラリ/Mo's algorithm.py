# Mo's algorithm
 
from math import sqrt, ceil
from sys import stdin
input = stdin.readline
 
n = int(input())
a = [color-1 for color in map(int, input().split())]
 
q = int(input())
# b: backet size
b = ceil(n / sqrt(2*q))
backets = [[] for _ in range(n//b + 1)]
#クエリの読み込みとバケット整理。ここでは正数の閉区間
for i in range(q):
    l, r = map(int, input().split())
    backets[(l-1)//b].append((l-1, r, i))
 
for i in range(len(backets)):
    backets[i].sort(key=lambda x: x[1], reverse=i&1)
 
cnt = 0
odd = [0] * n
ans = [0] * q
left = 0
right = 0
print(backets)
for backet in backets:
    for l, r, i in backet:
        while l < left:
            left -= 1
            ####################
            cnt += odd[a[left]]
            odd[a[left]] ^= 1
            #####################
        while right < r:
            ####################
            cnt += odd[a[right]]
            odd[a[right]] ^= 1
            ######################
            right += 1
        while left < l:
            #####################
            odd[a[left]] ^= 1
            cnt -= odd[a[left]]
            ######################
            left += 1
        while r < right:
            right -= 1
            ####################
            odd[a[right]] ^= 1
            cnt -= odd[a[right]]
            ####################
        ans[i] = cnt
 
print(*ans, sep='\n')