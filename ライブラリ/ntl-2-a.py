A,B = input().split()
def addition(a,b):
    if len(a)>len(b):
        a,b = b,a
    la = [int(a[i]) for i in reversed(range(len(a)))]+[0 for i in range(len(b)-len(a))]
    lb = [int(b[i]) for i in reversed(range(len(b)))]
    lab = []
    #k:繰り上がり
    k = 0
    for i in range(len(b)):
        dig = la[i]+lb[i]+k
        k=dig//10
        lab.append(dig%10)
    if k>0:
        lab.append(k)
    lab = [lab[i] for i in reversed(range(len(lab)))]
    return(lab)
def difference(a,b):
    la = [-int(a[i]) for i in reversed(range(len(a)))]+[0 for i in range(len(b)-len(a))]
    lb = [int(b[i]) for i in reversed(range(len(b)))]
    lab = []
    #k:繰り下がり
    k = 0
    for i in range(len(b)):
        dig = la[i]+lb[i]+k
        k=dig//10
        lab.append(dig%10)
    while len(lab)>1:
        if lab[-1]==0:
            lab.pop()
        else:
            break
    lab = [lab[i] for i in reversed(range(len(lab)))]
    return(lab)
if A[0]!="-" and B[0]=="-":
    B = B[1:]
    ans = addition(A,B)
elif A[0]=="-" and B[0]!="-":
    A = A[1:]
    ans = ["-"]+addition(A,B)
elif A[0]!="-" and B[0]!="-":
    if len(A)>len(B):
        ans = difference(B,A)
    elif len(A)==len(B) and A>=B:
        ans = difference(B,A)
    else:
        ans = ["-"]+difference(A,B)
else:
    B = B[1:]
    A = A[1:]
    if len(A)>len(B):
        ans = ["-"]+difference(B,A)
    elif len(A)==len(B) and A>B:
        ans = ["-"]+difference(B,A)
    else:
        ans = difference(A,B)
print(*ans,sep="")