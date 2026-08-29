h,w,n = map(int,input().split())
line_num = [-1 for i in range(h)]
column_num = [-1 for i in range(w)]
point = []
for i in range(n):
    r,c,a = map(int,input().split())
    point.append([a,r-1,c-1,i])
point.sort(reverse=True)
stock = []
last = 0
ans = [0 for i in range(n)]
for i in range(n):
    if point[i][0]==last:
        stock.append(point[i])
    else:
        last = point[i][0]
        for j in stock:
            ans[j[3]] = max(line_num[j[1]],column_num[j[2]])+1
        for j in stock:
            line_num[j[1]] = max(ans[j[3]],line_num[j[1]])
            column_num[j[2]] = max(ans[j[3]],column_num[j[2]])
        stock = [point[i]]

for j in stock:
    ans[j[3]] = max(line_num[j[1]],column_num[j[2]])+1
for j in stock:
    line_num[j[1]] = max(ans[j[3]],line_num[j[1]])
    column_num[j[2]] = max(ans[j[3]],column_num[j[2]])
for i in range(n):
    print(ans[i])
