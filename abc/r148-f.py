big = 1<<64
N = 1000000007
R = 998244353
divR = 996491785301655553
R2 = 320946142
Y = 18446744072709551609
M = 4915446
minus_one = 18446744073709551615
ans = []
a,b = 2,3
c = 0
def MR():
    global c
    ans.append("rem D T")
    ans.append("mul C D 4915446")
    ans.append("rem C C")
    ans.append("mul C C 1000000007")
    ans.append("add C C T")
    ans.append("mul C C 996491785301655553")
    d = t%R
    c = d*4915446%big
    c = c%R
    c = c*1000000007%big
    c = (c+t)%big
    c = c*996491785301655553%big
    #print(c)
    #N以下ならf = 0になっている。
    ans.append("rem E C")
    ans.append("add F C 1755654")
    ans.append("rem F F")
    ans.append("mul E E 18446744073709551615")
    ans.append("mul F F 18446744073709551615")
    ans.append("add E E C")
    ans.append("mul E E 996491785301655553")
    ans.append("add F F C")
    ans.append("mul F E F")
    ans.append("rem F F")
    #N以下ならf = 0になっている。
    e = c%R
    f= (c + 1755654)%big
    f = f%R
    e = e*18446744073709551615%big
    f = f*18446744073709551615%big
    e = (e+c)%big
    e = (e*996491785301655553)%big
    f = (f+c)%big
    #print(e,f)
    f = e*f%big
    f = f%R
    #以下、1,0にする
    ans.append("add I F 18446744073709551615")
    ans.append("rem I I")
    ans.append("add I I 66192444")
    ans.append("rem I I")
    ans.append("rem J F")
    ans.append("mul J J 18446744073709551615")
    ans.append("add J I J")
    ans.append("rem J J")
    ans.append("mul H J 165037813")
    ans.append("rem H H")
    i = (((f+18446744073709551615)%big)%R + 66192444)%big
    i = i%R
    j = f%R
    j = (j*18446744073709551615)%big
    j = j+i
    j = j%R
    h = (j*165037813)%big
    h = h%R
    #print(f,h)
    #1,0にしたものを引く
    ans.append("mul H H 18446744072709551609")
    ans.append("add C C H")
    h = h*18446744072709551609%big
    c = (c+h)%big
    #print(c)
#もう一回モンゴメリ乗算
ans.append("mul T A B")
t = a*b%big
MR()
ans.append("mul T C 320946142")
t = c*320946142%big
MR()
#print(c)
print(len(ans))
for i in range(len(ans)):
    print(ans[i])