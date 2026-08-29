B = int(input())
for a in range(1,18):
    if a**a==B:
        print(a)
        exit()
print(-1)