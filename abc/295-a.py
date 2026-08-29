N = int(input())
W = list(input().split())
print(W)
english = ["and","not","that","the","you"]
for word in english:
    if word in W:
        print("Yes")
        break
else:
    print("No")