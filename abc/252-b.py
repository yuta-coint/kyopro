N,K = map(int,input().split())
A= list(map(int,input().split()))
B= list(map(int,input().split()))
M = max(A)
yn = "No"
for i in range(N):
    if A[i]==M and i+1 in B:
        yn = "Yes"
print(yn)
