from collections import deque
def main(lines):
    S = lines[0]
    black = 0
    white = 0
    Board_state = deque([])
    for i in range(len(S)):
        if S[i]=="b":
            if white > 0:
                Board_state.append((white,-1))
                white = 0
            black += 1
        else:
            if black > 0:
                Board_state.append((black,1))
                black = 0
            white += 1
    if black > 0:
        Board_state.append((black,1))
    if white > 0:
        Board_state.append((white,-1))
    T = lines[1]
    L = len(Board_state)
    for i in range(len(T)):
        if i&1:
            turn = -1
        else:
            turn = 1
        hand = T[i]
        if hand == "L":
            edge, color = Board_state.popleft()
            if color == turn:
                Board_state.appendleft((edge + 1, color))
            else:
                if L==1:
                    Board_state.appendleft((edge, color))
                    Board_state.appendleft((1,turn))
                    L += 1
                else:
                    next_edge, next_color = Board_state.popleft()
                    Board_state.appendleft((1 + edge + next_edge, turn))
                    L -= 1
        else:
            edge, color = Board_state.pop()
            if color == turn:
                Board_state.append((edge + 1, color))
            else:
                if L==1:
                    Board_state.append((edge, color))
                    Board_state.append((1,turn))
                else:
                    next_edge, next_color = Board_state.pop()
                    Board_state.append((1 + edge + next_edge, turn))
    ans_black = 0
    ans_white = 0
    for edge, color in Board_state:
        if color == 1:
            ans_black += edge
        else:
            ans_white += edge
    print(ans_black, ans_white)
                    
                           
            
            
        