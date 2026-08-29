S = input()
T = input()
if len(S)>len(T):
    print("No")
elif S == T[:(len(S))]:
    print("Yes")
else:
    print("No")