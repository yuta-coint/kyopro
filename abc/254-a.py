N = int(input())
if N%100>9:
    print(N%100)
else:
    s = str(N%100)
    print("0"+s)