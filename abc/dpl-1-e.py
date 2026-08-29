s1 = input()
s2 = input()
Levenshtein = [[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
Levenshtein[0] = [j for j in range(len(s2)+1)]

for i in range(1,len(s1)+1):
    Levenshtein[i][0]=i
    for j in range(1,len(s2)+1):
        dif_character=1
        if s1[i-1]==s2[j-1]:
            dif_character=0
        Levenshtein[i][j]=min(Levenshtein[i][j-1]+1,Levenshtein[i-1][j]+1,Levenshtein[i-1][j-1]+dif_character)
print(Levenshtein[-1][-1])