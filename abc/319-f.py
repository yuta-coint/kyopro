#「倒せるやつ全員倒して薬を飲む」は確定なので、薬を飲む順番だけ考える。
#DPの値には、「強さいくつまでの敵を倒せるか」を持つ
N = int(input())
#子だけを表示する
G = [set() for i in range(N)]
pow_max = []
portion = []
por_ind = [0]
enemy = [-1]
mother = [-1]
for i in range(1,N):
    p,t,s,g = map(int,input().split())
    if t==1:
        enemy.append((s,g))
    else:
        enemy.append((s,-1))
        portion.append((i,g))
        por_ind.append(i)
    G[p-1].add(i)
    mother.append(p-1)
cnt_p = len(portion)
#先に飲んでおく薬を書いておく
mother_portion = []
set_por_ind = set(por_ind)
for i in por_ind:
    temp = i
    while True:
        if temp in set_por_ind:
            mother_portion.append(temp)
            break
        temp = mother[temp]
for drunk in range(1<<cnt_p):
    #各成分について順序の正当性を確認する

    #そのあと、それぞれをひとつずつ抜いて、倒せるものがないか確かめる？
