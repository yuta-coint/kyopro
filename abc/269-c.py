import sys
sys.setrecursionlimit(10**6)
N = int(input())
def out(base,digit):
    #print(base,digit)
    if digit == -1:
        print(base)
    elif (N>>digit)&1:
        out(base,digit-1)
        out(base+(1<<digit),digit-1)
    else:
        out(base,digit-1)
out(0,61)