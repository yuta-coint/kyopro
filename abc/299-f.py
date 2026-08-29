S = list(input())
ls = len(S)
S = [ord(S[i])-ord("a") for i in range(len(S))]
chk = [-1 for i in range(26)]
pre = []
#ひとつ前の同じ文字はどこですか？
for i in range(ls):
    pre.append(chk[S[i]])
    chk[S[i]]=i  
ans = 0
mod = 998244353
for cut in range(1,len(S)):
    back = S[cut:]
    front = S[:cut]
    sqs = [[0 for j in range(cut)] for i in range(ls-cut)]
    sqs_sum = [[0 for j in range(cut+1)] for i in range(ls-cut+1)]
    for i in range(ls-cut):
        if i==0:
            for j in range(cut):
                if back[0]==front[j]:
                    sqs[0][j]=1
                sqs_sum[1][j+1]=sqs_sum[1][j]+sqs[0][j]
            continue
        for j in range(cut):
            if back[i]==front[j]:
                sqs[i][j]=sqs_sum[i-1][j-1]
            sqs_sum[i+1][j+1]=(sqs_sum[i][j+1]+sqs_sum[i+1][j]-sqs_sum[i][j]+sqs[i][j])%mod
    ans+=sqs_sum[ls-cut][cut]
    ans%=mod
print(ans)