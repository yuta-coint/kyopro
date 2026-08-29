import time
time.perf_counter()
N,M = map(int,input().split())
C=[[0 for i in range(N+2)]]+[[0]+list(map(int,input().split()))+[0] for i in range(N)]+[[0 for i in range(N+2)]]
from collections import deque
# --- ここから追加 ---
import copy

# 初期の隣接関係を取得
original_adj = set()
for i in range(1, N+1):
    for j in range(1, N+1):
        c = C[i][j]
        for dx, dy in [(1,0), (0,1)]:
            ni, nj = i+dx, j+dy
            if ni <= N and nj <= N:
                c2 = C[ni][nj]
                if c != c2:
                    original_adj.add((min(c, c2), max(c, c2)))
        # 外周（色0）との隣接
        if i == 1 and c != 0: original_adj.add((0, c))
        if i == N and c != 0: original_adj.add((0, c))
        if j == 1 and c != 0: original_adj.add((0, c))
        if j == N and c != 0: original_adj.add((0, c))

def check_valid(C_test):
    visited = [[False]*(N+2) for _ in range(N+2)]
    color_counts = [0] * (M + 1)
    for i in range(1, N+1):
        for j in range(1, N+1):
            color_counts[C_test[i][j]] += 1
    
    found_colors = [0] * (M + 1)
    test_adj = set()
    for i in range(1, N+1):
        for j in range(1, N+1):
            c = C_test[i][j]
            # 隣接関係の構築
            for dx, dy in [(1,0), (0,1)]:
                ni, nj = i+dx, j+dy
                if ni <= N and nj <= N:
                    c2 = C_test[ni][nj]
                    if c != c2:
                        test_adj.add((min(c, c2), max(c, c2)))
            if i == 1 and c != 0: test_adj.add((0, c))
            if i == N and c != 0: test_adj.add((0, c))
            if j == 1 and c != 0: test_adj.add((0, c))
            if j == N and c != 0: test_adj.add((0, c))
            
            # 各色の連結性チェック
            if c > 0 and not visited[i][j]:
                if found_colors[c] > 0: return False
                q = deque([(i, j)])
                visited[i][j] = True
                cnt = 0
                while q:
                    cx, cy = q.popleft()
                    cnt += 1
                    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                        nx, ny = cx+dx, cy+dy
                        if 1 <= nx <= N and 1 <= ny <= N:
                            if not visited[nx][ny] and C_test[nx][ny] == c:
                                visited[nx][ny] = True
                                q.append((nx, ny))
                found_colors[c] += 1
                if cnt != color_counts[c]: return False
    
    # 隣接関係の完全一致チェック
    if test_adj != original_adj: return False
    
    # 色0の連結性チェック（外周からBFS）
    q = deque()
    visited_zero = [[False]*(N+2) for _ in range(N+2)]
    for i in range(N+2):
        q.append((0, i)); visited_zero[0][i] = True
        q.append((N+1, i)); visited_zero[N+1][i] = True
        q.append((i, 0)); visited_zero[i][0] = True
        q.append((i, N+1)); visited_zero[i][N+1] = True
        
    connected_zeros = 0
    while q:
        cx, cy = q.popleft()
        if 1 <= cx <= N and 1 <= cy <= N:
            connected_zeros += 1
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = cx+dx, cy+dy
            if 0 <= nx <= N+1 and 0 <= ny <= N+1:
                if not visited_zero[nx][ny] and C_test[nx][ny] == 0:
                    visited_zero[nx][ny] = True
                    q.append((nx, ny))
                    
    if connected_zeros != color_counts[0]:
        return False
        
    return True

# 行の圧縮（上に詰める処理と下に詰める処理を両方試行）
for r in range(1, N+1):
    C_test = [row[:] for row in C]
    for i in range(r, N): C_test[i] = C_test[i+1][:]
    C_test[N] = [0]*(N+2)
    if check_valid(C_test):
        C = C_test
        continue
        
    C_test = [row[:] for row in C]
    for i in range(r, 1, -1): C_test[i] = C_test[i-1][:]
    C_test[1] = [0]*(N+2)
    if check_valid(C_test): C = C_test

# 列の圧縮（左に詰める処理と右に詰める処理を両方試行）
for c_idx in range(1, N+1):
    C_test = [row[:] for row in C]
    for i in range(1, N+1):
        for j in range(c_idx, N): C_test[i][j] = C_test[i][j+1]
        C_test[i][N] = 0
    if check_valid(C_test):
        C = C_test
        continue
        
    C_test = [row[:] for row in C]
    for i in range(1, N+1):
        for j in range(c_idx, 1, -1): C_test[i][j] = C_test[i][j-1]
        C_test[i][1] = 0
    if check_valid(C_test): C = C_test
# --- ここまで追加 ---
edge_tiles = deque()
#これの正負が変わらないようにする
rinsetsu = [[0 for i in range(M+1)] for j in range(M+1)]
#とりあえず端から削れるところ削っていくか
#周りにあるのが0と自分であるようなやつらを消していく
mawari = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1)]
sayuu = [(0,-1),(0,1),(-1,0),(1,0)]
for i in range(N-1):
    for x,y in ([(1,i+1),(i+1,N),(N,N-i),(N-i,1)]):
        edge_tiles.append((x,y))
visited = [[False for i in range(N+2)] for j in range(N+2)]
while edge_tiles:
    x,y = edge_tiles.popleft()
    visited[x][y]=True
    chk_zero = 0
    chk_c = 0
    for p,q in mawari:
        if C[x+p][y+q]==0:
            chk_zero +=1
        elif C[x+p][y+q]==C[x][y]:
            chk_c +=1
        else:
            break
    else:
        if chk_c>0 and chk_zero>0:
            C[x][y]=0
            for p,q in sayuu:
                if C[x+p][y+q]==0:
                    continue
                if visited[x+q][y+q]:
                    continue
                edge_tiles.append((x+p,y+q))
#外周9マス見て、三色で、真ん中を抜いても連結が保たれるなら、真ん中を一番外側の色に変える
#四色だった時の処理が難しい
from random import random
for _ in range(1000):
    for i in range(1,N+1):
        for j in range(1,N+1):
            center = True
            cnt = 0
            for t in range(-1,7):
                if C[mawari[t][0]+i][mawari[t][1]+j]!=C[mawari[t+1][0]+i][mawari[t+1][1]+j]:
                    cnt+=1
                if C[mawari[t][0]+i][mawari[t][1]+j]==C[i][j]:
                    center = False
            if center:
                continue
            if cnt>4:
                continue
            if cnt==4:
                c1,c2,c3,c4,c5,c6,c7,c8,c9 = C[i-1][j-1],C[i-1][j],C[i-1][j+1],C[i][j-1],C[i][j],C[i][j+1],C[i+1][j-1],C[i+1][j],C[i+1][j+1]
                if len(set([c1,c2,c3,c4,c5,c6,c7,c8,c9]))<4:
                    continue
                chk1 = set()
                chk2 = set()
                for p,q in ([(c1,c4),(c4,c7),(c7,c8),(c8,c9),(c9,c6),(c6,c3),(c3,c2),(c2,c1)]):
                    chk1.add(p*(10**6)+q)
                    chk1.add(q*(10**6)+p)
                    chk2.add(p*(10**6)+q)
                    chk2.add(q*(10**6)+p)
                for q in ([c2,c4,c6,c8]):
                    chk1.add(c5*(10**6)+q)
                    chk1.add(q*(10**6)+c5)
                if i+(random()-0.5)*4>j and i+j+(random()-0.5)*4>50:
                    r = C[i+1][j]
                elif i+j+(random()-0.5)*4>50:
                    r = C[i][j+1]
                elif i+(random()-0.5)*4>j:
                    r= C[i][j-1]
                else:
                    r = C[i-1][j]
                for q in ([c2,c4,c6,c8]):
                    chk2.add(r*(10**6)+q)
                    chk2.add(q*(10**6)+r)
                if chk1==chk2:
                    C[i][j]=r
                continue
            if C[i+1][j]==0 or C[i][j+1]==0 or C[i][j-1]==0 or C[i-1][j]==0 and random()>1-i*(0.001):
                C[i][j]=0
            elif i+(random()-0.5)*4>j and i+j+(random()-0.5)*4>50:
                C[i][j] = C[i+1][j]
            elif i+j+(random()-0.5)*4>50:
                C[i][j] = C[i][j+1]
            elif i+(random()-0.5)*4>j:
                C[i][j]= C[i][j-1]
            else:
                C[i][j] = C[i-1][j]
        # --- ここから追加 ---
        # 毎回実行するとTLEになるため、50回に1回の頻度で行/列の削除を試みる
        if _ % 50 == 0:
            # 行の圧縮
            for r in range(1, N+1):
                C_test = [row[:] for row in C]
                for i in range(r, N): C_test[i] = C_test[i+1][:]
                C_test[N] = [0]*(N+2)
                if check_valid(C_test):
                    C = C_test
                    continue
                    
                C_test = [row[:] for row in C]
                for i in range(r, 1, -1): C_test[i] = C_test[i-1][:]
                C_test[1] = [0]*(N+2)
                if check_valid(C_test): C = C_test

            # 列の圧縮
            for c_idx in range(1, N+1):
                C_test = [row[:] for row in C]
                for k in range(1, N+1):
                    for j in range(c_idx, N): C_test[k][j] = C_test[k][j+1]
                    C_test[k][N] = 0
                if check_valid(C_test):
                    C = C_test
                    continue
                    
                C_test = [row[:] for row in C]
                for k in range(1, N+1):
                    for j in range(c_idx, 1, -1): C_test[k][j] = C_test[k][j-1]
                    C_test[k][1] = 0
                if check_valid(C_test): C = C_test
        # --- ここまで追加 ---
for i in range(1,N+1):
    print(*C[i][1:N+1])
#乱択山登りしたいなあ