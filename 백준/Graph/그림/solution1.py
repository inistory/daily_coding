from collections import deque 
import sys

dr, dc = [1,-1,0,0], [0,0,1,-1]

def bfs(board, i,j):
    count = 1 
    board[i][j] = 0 #count하고 난 다음에는 board에 0을 대입
    queue = deque([[i,j]])
    while queue:
        r,c = queue.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0<=nr<len(board) and 0<=nc<len(board[0]):
                if board[nr][nc] ==1:
                    board[nr][nc] = 0
                    count +=1 
                    queue.append([nr,nc])
    return count

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int,  sys.stdin.readline().split())) for i in range(N)]
lengths = [] 
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            lengths.append(bfs(board, i, j))

if lengths:
    print(len(lengths))
    print(max(lengths))
else:
    print(0)
    print(0)