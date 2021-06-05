def solution(boards, moves):
    moves = list(map(lambda x : x-1, moves)) #1씩 빼주기
    print(moves)
    stack = [0] #index out of range 방지하여 0 넣어주기
    cnt = 0
    for  i in moves:
        for board in boards:
            if board[i] != 0:
                stack.append(board[i]) #뽑은 수를 스택에 넣기
                board[i] = 0
                # print(stack)
                if stack[-1] == stack[-2]: #스택의 가장위, 그 아래 수를 비교
                    stack.pop()
                    stack.pop()
                    cnt+=2 #두 개씩 사라지니까
                break # 0으로 바꾼 후 다음 배열로 넘어가지 않도록
    return cnt