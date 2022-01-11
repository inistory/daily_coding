def solution(boards, moves):
    moves = list(map(lambda x : x-1, moves)) #1씩 빼주기
    stack = [0] #index out of range 방지하여 0 넣어주기(맨 처음에도 stack[-2]를 검사할경우에 발생)
    cnt = 0
    for i in moves:
        for board in boards:
            if board[i] !=0:
                stack.append(board[i])
                board[i] = 0
                if stack[-1] == stack[-2]:  #스택의 가장위, 그 아래 수를 비교
                    stack.pop()
                    stack.pop()
                    cnt+=2
                break
    return cnt