def main():
    import sys
    input = sys.stdin.readline
    H,W = map(int,input().split())
    S = [input() for i in range(H)]
    T = [input() for i in range(H)]
    Sim  = []
    Tim = []
    for j in range(W):
        s = []
        t = []
        for i in range(H):
            s.append(S[i][j])
            t.append(T[i][j])
        Sim.append(s)
        Tim.append(t)
    Sim.sort()
    Tim.sort()
    if Sim == Tim:
        print("Yes")
    else:
        print("No")
main()