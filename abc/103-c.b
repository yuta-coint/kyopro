s = input()
t = input()
l = len(s) #文字列の長さを取得
flag = 0
for i in range(l):
    f = s[:1] #一文字目を切り取る
    s = s[1:] + f #一文字目を削る
    if s == t:
        flag = 1
        break
if flag == 1:
    print('Yes')
else:
    print('No')
