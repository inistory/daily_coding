def step(board, moves):
    """moves(i,j,board) -> [(ni,nj,val), ...] : (i,j)의 결과 목적지와 누적값"""
    n, m = len(board), len(board[0])
    nxt = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for ni, nj, val in moves(i, j, board):
                nxt[ni][nj] += val      # 여러 소스가 한 칸에 모이면 합쳐짐(합류/충돌 규칙 자리)
    return nxt

