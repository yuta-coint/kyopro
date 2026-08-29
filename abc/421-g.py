from pulp import LpStatus,LpVariable,LpProblem,LpMinimize,lpSum, PULP_CBC_CMD
N, M = map(int,input().split())
A = list(map(int,input().split()))
LR = [tuple(map(int,input().split())) for i in range(M)]

prob =  LpProblem(sense = LpMinimize)
x = LpVariable.dicts("x",(range(M),), lowBound = 0)
chk_plus = [[] for i in range(N-1)]
chk_minus = [[] for i in range(N-1)]
for i in range(M):
    l,r = LR[i]
    l -= 1
    r -= 1
    if l >= 1:
        chk_plus[l-1].append(i)
    if r < N-1:
        chk_minus[r].append(i)
for i in range(N-1):
    prob += lpSum([x[j] for j in chk_plus[i]]) - lpSum([x[j] for j in chk_minus[i]]) + A[i+1] - A[i] >= 0
    #for t in chk_minus[i]:
    #    print(i,t)
prob += lpSum([x[j] for j in range(M)])
prob.solve(PULP_CBC_CMD(msg=0))
#for name, constraint in prob.constraints.items():
#    print(f"制約名: {name}")
#    print(f"制約式: {constraint}")
#    print("-" * 20)

if LpStatus[prob.status] != 'Infeasible':
    print(int(prob.objective.value()))
    #for i in range(N-1):
    #    print(f"x[{i}]: {x[i].value()}")
else:
    print(-1)