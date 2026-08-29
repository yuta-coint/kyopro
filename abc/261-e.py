import sys
input = sys.stdin.readline
def main():
    N,C = map(int,input().split())
    live = 0
    and_or = 0
    xor_sum = 0
    All_xor = 0
    part_xor = 0
    INF = (1<<31) -1
    for _ in range(N):
        T,A = map(int,input().split())
        if T==1:
            xor_sum &= A
            and_or &= A
            live |= INF-A
        elif T==2:
            xor_sum &= INF-A
            and_or |= A
            live |= A
        else:
            xor_sum ^= A
            part_xor^= A
        All_xor^=part_xor
        print((live & (and_or ^ xor_sum))|((C ^ All_xor) & (INF-live)))
main()