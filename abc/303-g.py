from collections import deque
def Sliding_mimimum_elements(K,L,a):
    window = deque([])
    r = (a[0],0)
    ans = []
    #どこの値かの復元
    ind = []
    for i in range(K):
        f = 0
        if window:
            r=window.pop()
            f = 1
        while r[0]>a[i] and window:
            r=window.pop()
        if (r[0]<=a[i] or i==0) and f==1:
            window.append(r)
        window.append((a[i],i))
        if i<L-1:
            continue
        ans.append(window[0][0])
        ind.append(window[0][1])
        if window[0][1]<=i+1-L:
            window.popleft()
    return ans
N,A,B,C,D = map(int,input().split())
x = list(map(int,input().split()))
x_sum = [0]
taka = 0
aoki = 0
for i in range(N):
    x_sum.append(x_sum[-1]+x[i])
#長さ1がN通りなら0はN+1通り
ans_taka = [[0 for i in range(N+1)]]
for win in range(1,N+1):
    #aokiが左から一個とるか右から一個とるか全部取るか
    ans = []
    for i in range(N-win+1):
        #[i,i+win)
        ans.append(max(x[i]-ans_taka[win-1][i+1],x[i+win-1]-ans_taka[win-1][i]))
    if win<=D:
        ans_b = [x_sum[i+win]-x_sum[i]-C for i in range(N-win+1)]
    else:
        #D個減らす操作で一番ましなのを考える
        #長さwin-Dの幅の長さと相手から見た
        next_turn = [-x_sum[i]+x_sum[i+win-D]+ans_taka[win-D][i] for i in range(N+1-win+D)]
        ans_b = Sliding_mimimum_elements(N+1-win+D,D+1,next_turn)
        for i in range(N-win+1):
            ans_b[i] = x_sum[i+win]-x_sum[i]-ans_b[i]-C
    for i in range(N-win+1):
        if ans[i]<ans_b[i]:
            ans[i] = ans_b[i]
    if win<=B:
        ans_b = [x_sum[i+win]-x_sum[i]-A for i in range(N-win+1)]
    else:
        #D個減らす操作で一番ましなのを考える
        next_turn = [-x_sum[i]+x_sum[i+win-B]+ans_taka[win-B][i] for i in range(N+1-win+B)]
        ans_b = Sliding_mimimum_elements(N+1-win+B,B+1,next_turn)
        for i in range(N-win+1):
            ans_b[i] = x_sum[i+win]-x_sum[i]-ans_b[i]-A
    for i in range(N-win+1):
        if ans[i]<ans_b[i]:
            ans[i] = ans_b[i]
    ans_taka.append(ans)
#print(ans_taka)
#print(ans_aoki)
print(ans_taka[-1][0])