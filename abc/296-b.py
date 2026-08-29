file = list("abcdefgh")
rank = [8-i for i in range(8)]
for i in range(8):
    S = input()
    for j in range(8):
        if S[j]=="*":
            print(file[j]+str(rank[i]))
            exit()