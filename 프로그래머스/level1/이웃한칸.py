def solution(board, h, w):
    #2차원 격자 보드판
    #한칸 골랐을 때 위아래오른쪽왼쪽 중에서 같은 색으로 칠해진 칸의 개수 구함
    n = len(board)
    count = 0
    dh = [0,1,-1,0]
    dw = [1,0,0,-1]
    
    for i in range(4):
        h_check = h + dh[i]
        w_check = w + dw[i]
        if 0<= h_check<n and 0<=w_check<n:
            if board[h][w] == board[h_check][w_check]:
                count+=1
    return count