from math import sqrt
import sys
ssf = sys.stdout.flush
#上に凸な単峰関数を仮定する
Fibonacci = [1,1]
for i in range(15):
    Fibonacci.append(Fibonacci[i]+Fibonacci[i+1])
def query(i):
    if i in check:
        return check[i]
    else:
        print("?",i)
        ssf()
        Ai = int(input())
        check[i]=Ai
        return Ai
for case in range(int(input())):
    N=int(input())
    check = {}
    l = 0
    r = 1597
    check[0]=-1
    for k in range(N+1,1597):
        check[k]=-1
    for j in reversed(range(1,15)):
        templ = l+Fibonacci[j]
        tempr = r-Fibonacci[j]
        ql = query(templ)
        qr = query(tempr)
        if ql>=qr:
            r=tempr
        else:
            l=templ
    print("!",max(check[templ],check[tempr]))