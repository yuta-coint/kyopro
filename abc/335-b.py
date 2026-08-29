N = int(input())
for x in range(30):
    for y in range(30):
        for z in range(30):
            if x+y+z<=N:
                print(x,y,z)