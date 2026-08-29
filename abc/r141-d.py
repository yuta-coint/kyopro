import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
map(int,input().split())