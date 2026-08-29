s = input()
n=len(s)
if s[0]==s[-1]:
    n+=1
if n%2==0:
    print("Second")
else:
    print("First")