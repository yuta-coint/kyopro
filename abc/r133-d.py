l,r,v = map(int,input().split())
mod = 998244353
#半開区間に書き換えておく
l-=2
#l<s<t<=r
#RとLの累積和の和がvとなるものを数える。
#4n+1までは1,4n+2までは4n+3,4n+3までは0,4nまでは4n
ans = 0
#左が4の倍数
#4で割った余りの組み合わせ
#4n+1は何個あるか
count1 = ((r+3)//4-(l+3)//4)%mod
#4n+3は何個あるか
count0 = ((r+1)//4-(l+1)//4)%mod
if v ==0:
    ##11,33は何れも0になる
    ans+=(count0*(count0-1)//2)%mod
    ans+=(count1*(count1-1)//2)%mod
    ans%=mod
elif v==1:
    #13,31は何れも1になる
    ans+=(count1*count0)%mod
#01と10は4n+1
if v%4==1 and l<v-1<=r:
    ans+=count1
    ans%=mod

#12と21は4n+2になる
if v%4==2 and l<v<=r:
    ans+=count1
    ans%=mod

#23と32は4n+3,v-1
if v%4==3 and l<v-1<=r:
    ans+=count0
    ans%=mod

#03と30は4n,v
if v%4==0 and l<v<=r:
    ans+=count0
    ans%=mod
#最も非自明な6ケース。
#s未満とt未満からひとつずつ取ってきてxorがuになる組み合わせは何通りですか？
def xorcount2(s,t,u):
    if s>t:
        s,t = t,s
    if s==0:
        return 0
    if t==1 and u==0:
        return 1
    keta = len(bin(t-1))-3
    if (1<<(keta+1))<=u:
        return 0
    if (u>>keta)&1:
        if ((s-1)>>keta)&1:
            return (s+t-(1<<(keta+1)))%mod
        else:
            return xorcount2(s,t-(1<<keta),u-(1<<keta))%mod
    else:
        if ((s-1)>>keta)&1:
            return ((1<<keta)+xorcount2(s-(1<<keta),t-(1<<keta),u))%mod
        else:
            return s
#[s,t)から相異なる二つとってきてxorがuになる組み合わせは何通りですか？
half = pow(2,mod-2,mod)
def xorcount(s,t,u):
    return (xorcount2(t,t,u)-xorcount2(s,t,u)*2+xorcount2(s,s,u))*half%mod
a = v>>2
##22…4n^4n
if v%4==0 and v>0:
    ans+=xorcount((l+2)>>2,(r+2)>>2,a)
    ans%=mod
##00…4n^4n
if v%4==0 and v>0:
    ans+=xorcount((l+4)>>2,(r+4)>>2,a)
    ans%=mod

##24,42…4n^4n+3
#v>3のとき、相異なる二つをとってきて二倍すればいい
if v%4==3 and v>3:
    ans += xorcount((l+4)>>2,(r+2)>>2,a)*2
    #小さい方にはみ出た4n+2を使うルート
    if l%4==0:
        if l<(l+2)^v<=r:
            ans+=1
    if l%4==1:
        if l<(l+1)^v<=r:
            ans+=1
    #大きい方にはみ出た4nを使うルート
    if r%4==0:
        if l<(r^v)-1<=r:
            ans+=1
    if r%4==1:
        if l<((r-1)^v)-1<=r:
            ans+=1
    ans%=mod
if v==3:
    #4nと4n+2の組み合わせを数え上げる
    ans+=(r-2)//4-l//2
    ans%=mod
print(ans)