def main():
    S = list(input())
    L = len(S)
    broken = [-1 for i in range(L)]
    stk = []
    for i in reversed(range(L)):
        if S[i]==")":
            stk.append(i)
        elif S[i]=="(":
            broken[i]=stk.pop()
    #print(broken)
    stk = [L+1]
    last = [-1 for i in range(26)]
    ans = "Yes"
    for i in range(L):
        #print(stk)
        if S[i]=="(":
            stk.append(broken[i])
        elif S[i]==")":
            stk.pop()
        else:
            if i<last[ord(S[i])-ord("a")]:
                ans = "No"
                break
            else:
                last[ord(S[i])-ord("a")] = stk[-1]
    print(ans)
main()


