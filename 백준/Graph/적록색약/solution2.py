import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
#상하좌우로 움직이는 좌표
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x,y):
    visited[x][y] = 1 #4)좌표를 방문표시
    #5)상하좌우로 이동할 수 있도록 순차적으로 값을 대입
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        #6)한구역에 속할 수 있는지 검사
        if (0 <= nx < n) and (0 <= ny < n):#board 범위 내의 값만 확인하기 위함
            if board[nx][ny] == board[x][y] and visited[nx][ny]==0:
                dfs(nx,ny)#7)같은 구역에 속해있다면 dfs에 좌표전달

#1)입력
n = int(input().rstrip())
board = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j]==0: #2)방문 전이면
            dfs(i,j) #3)해당 좌표를 전달
            cnt += 1 #8)dfs에서 한 구역을 돌았으니, cnt+1
print(cnt, end=' ')

#적색과 녹색이 동일하도록 변경
for i in range(n):
    for j in range(n):
        if board[i][j]=='R':
            board[i][j]='G'

visited = [[0] * n for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i,j)
            cnt += 1

print(cnt)