N = int(input())
S = list(input())
if not("A" in S):
    for i in range(N):
        print("Bob")
    exit()
if not("B" in S):
    for i in range(N):
        print("Alice")
    exit()
for i in range(N+1):
    if S[i]=="A":
        mi_a = i
        break
for i in range(N+1):
    if S[i]=="B":
        mi_b = i
        break
#print(mi_a)
#print(mi_b)
for i in range(1,1+N):
	if i&1:
		for j in range(mi_b+1,N+1):
			if S[j]=="B":
				mi_b=j
				break
		else:
			for k in range(i,1+N):
				print("Alice")
			exit()
	else:
		for j in range(mi_a+1,N+1):
			if S[j]=="A":
				mi_a=j
				break
		else:
			for k in range(i,1+N):
				print("Bob")
			exit()
	if mi_a<mi_b:
		print("Alice")
	else:
		print("Bob")