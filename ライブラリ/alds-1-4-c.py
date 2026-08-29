n =  int(input())
d = {}
for i in range(n):
    a,b = input().split()
    if a == "insert":
        d[b]="yes"
    else:
        if b in d:
            print("yes")
        else:
            print("no")

