S = input()
T = input()
ls = len(S)
lt = len(T)
stk = 1
k = 0
Sc = []
Sl = []
for i in range(ls):
    if S[i]==k:
        stk+=1
    else:
        Sc.append(stk)
        stk=1
        k=S[i]
        Sl.append(k)
Sc.append(stk)
Tc = []
Tl = []
k=0
stk=1
for i in range(lt):
    if T[i]==k:
        stk+=1
    else:
        Tc.append(stk)
        stk=1
        k=T[i]
        Tl.append(k)
Tc.append(stk)
#print(Sl)
#print(Sc)
#print(Tl)
#print(Tc)
if Sl!=Tl:
    print("No")
else:
    for i in range(len(Sc)):
        if Sc[i]==1:
            if Tc[i]!=1:
                print("No")
                break
        else:
            if Tc[i]<Sc[i]:
                print("No")
                break
    else:
        print("Yes")