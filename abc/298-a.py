N = int(input())
s = list(input())
good = s.count("o")
bad = s.count("x")
if good>0 and bad==0:
    print("Yes")
else:
    print("No")