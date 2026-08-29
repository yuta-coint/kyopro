#i枚目の壁を破壊する段階で負の座標にあるハンマーj個以上持っている時最短距離はいくらか
N,X=map(int,input().split())
Y = list(map(int,input().split()))
Z = list(map(int,input().split()))
minus_walls = []
plus_walls = []
plus_hammer = []
minus_hammer = []
#各ハンマーの取得に壁を何枚破壊する必要があるか
for i in range(N):
    if Y[i]<0:
        minus_walls.append((Y[i],i))
    else:
        plus_walls.append((Y[i],i))
    if Z[i]<0:
        minus_hammer.append(Z[i])
    else:
        plus_hammer.append(Z[i])   
d = {}
"""次の壁を破壊する上ではハンマーが必要
⇒壁の番号とハンマーの位置を検索
j個めのハンマーを持っているだけではそもそもi枚目の壁を破壊することができない可能性がある
各ハンマーについて回収するために右にどれくらい進んでいないといけないかを検索できるようにする
⇒何個目のハンマーまで持っていれば破壊できるor左のハンマーだけで破壊できるor右にハンマーがあるために破壊不可能
#すでに必要なハンマーが回収されており、間の距離を移動するだけで事足りる
ハンマーが左(k)個めの時
dp[i-1][k]+(間の距離)
#まっすぐ左のハンマーに向かっていけばそのハンマーが回収できる
dp[i-1][0]+(ハンマーまでの距離)+(ハンマーからの距離)
#左の壁を壊すためにいったん右に行く必要がある
dp[i-1][0]+(取らなきゃいけないハンマーまで)+(ハンマーまでの距離)+(ハンマーからの距離)
#そのハンマーまでたどり着けない
"""
#i枚目の壁に対応するハンマーは何番目でどこにあるか（正負両方！）
#
dp = [[float('inf') for j in range(N)] for i in range(N)]
for i in range(N):
    for j in range(N):
        if 
