T = int(input())
#重なっている部分を貪欲にずらしていきたいところだが、
#順序が決まれば貪欲に左端に揃えていけば良いのだが、
#コンピュータに任せるべき話なのかもしれない…
for _ in range(T):
    N = int(input())
    D = int(input())
    buttons = []
    for i in range(N):
        t,x = map(int,input().split())
        buttons.append((t-x,2))

map(int,input().split())