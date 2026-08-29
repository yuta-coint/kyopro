mod = 998244353
fact = [1]
for i in range(1,10**6):
    fact.append(fact[-1]*i%mod)
fact_rev = [pow(fact[-1],mod-2,mod)]
for i in reversed(range(1,10**6)):
    fact_rev.append(fact_rev[-1]*i%mod)
fact_rev.reverse()
S = list(input())
N = len(S)
##同じのが二回出てくるタイミングがあるかないか
flag = N
alr = set()
for i in range(N):
    if 0<= ord(S[i])-ord("A")<26:
        if S[i] in alr:
            flag = i
            break
        else:
            alr.add(S[i])
#n文字目までにDDがあるやつを調べる
pow52 = [1]
pow26 = [1]
for i in range(10**6):
    pow52.append(pow52[-1]*52%mod)
    pow26.append(pow26[-1]*26%mod)
def DD_check(capi,ques):
    #大文字がすべて相異なるようなものを数えて全体から引く
    temp = 0
    for c in range(min(26-capi,ques)+1):
        #大文字がc種、小文字がques-c個。どこを大文字にするか→小文字の内容→大文字の内容
        temp+=fact[ques]*fact_rev[c]%mod*fact_rev[ques-c]%mod*pow26[ques-c]%mod*fact[26-capi]%mod*fact_rev[26-c-capi]%mod
        temp%=mod
    return((pow52[ques]-temp)%mod)
question_count = 0
DD_sum = [0]
capital = 0
for i in range(flag):
    if 0<=ord(S[i])-ord("a")<26:
        pass
    #前に含まれている大文字の数から
    elif S[i]=="?":
        question_count+=1
    else:
        capital+=1
    DD_sum.append(DD_check(capital,question_count))
#flagから先は何やってもDDができる
for i in range(flag,N):
    if S[i]=="?":
        question_count+=1
    DD_sum.append(pow52[question_count])
DDo_sum = [0]
DDoS_sum = [0]
for i in range(N):
    if 0<=ord(S[i])-ord("a")<26:
        DDo_sum.append(DD_sum[i])
        DDoS_sum.append(DDoS_sum[-1])
    elif S[i]=="?":
        DDo_sum.append((DDo_sum[-1]*26+DD_sum[i]*26)%mod)
        DDoS_sum.append((DDoS_sum[-1]*26+DDo_sum[i]*26)%mod)
    else:
        DDo_sum.append(DDo_sum[-1])
        DDoS_sum.append(DDo_sum[i])
#print(DD_sum)
#print(DDo_sum)
#print(DDoS_sum)
print((pow52[question_count]-DDoS_sum[-1])%mod)
#print(DDoS_sum[-1])
#for i in range(N):
#    print([DD_check(i,j) for j in range(N)])