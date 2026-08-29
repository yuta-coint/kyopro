moji = "ABCDEFG"
num = [0,3,4,8,9,14,23]
points = {moji[i]:num[i] for i in range(7)}
pq = list(input().split())
print(abs(points[pq[0]]-points[pq[1]]))