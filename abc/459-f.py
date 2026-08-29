from pulp import LpProblem, LpVariable,  LpMinimize, lpSum, PULP_CBC_CMD
from math import floor, ceil
def solve():
    N = int(input())
    A = list(map(int,input().split()))
    B = [A[i + 1] - A[i] for i in range(N - 1)]
    p = LpVariable.dicts("p", (range(N + 1),), lowBound=0)
    prob = LpProblem(sense=LpMinimize)
    for i in range(1, N):
        prob += 2 * p[i] - p[i - 1] - p[i + 1] - 1 + B[i - 1] >= 0
    prob += p[0] == 0
    prob += p[N] == 0
    prob += lpSum(p)
    prob.solve(PULP_CBC_CMD(msg=0))
    ans = 0
    for i in range(1,N):
        ans += ceil(p[i].value())
    print(ans)
T = int(input())
for case in range(T):
    solve()
