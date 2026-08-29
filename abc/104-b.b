s=input()
flag =1
a=s[0]
b=s[2:-1]
if 'C' in b:
    flag=flag
else:
    flag = 2
if a!='A':
    flag=2
t=0
l=len(s)
for i in range(l):
    j=s[i]
    if j.islower():
        t=t+1
if t == 2:
    flag = 2
if flag == 1:
    print('AC')
else:
    print('WA')
