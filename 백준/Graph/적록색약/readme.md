## 1. 문제 설명

[문제 링크](https://www.acmicpc.net/problem/10026)

- 첫째 줄: N (가로, 세로 크기)
- 다음 N개 줄: 그림 정보
- return : 적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수

## 2. 코드

- BFS 코드

```python
from collections import deque

#상하좌우로 움직이는 좌표
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q.append([x, y]) #4)좌표 값을 큐에 넣음
    while q: #5)큐에 있는 값: 처음제공된 좌표의 값과 같은 색인 좌표들이 없을 때까지 반복
        x, y = q.popleft() #6)큐에서 값를 꺼냄
        #7)상하좌우로 이동할 수 있도록 순차적으로 값을 대입
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #8)한구역에 속할 수 있는지 검사
            if 0 <= nx < n and 0 <= ny < n: #board 범위 내의 값만 확인하기 위함
                if board[nx][ny] == board[x][y] and visited[nx][ny] == 0: #현재 좌표의 색상과 상하좌우 좌표에 있는 색상이 같고, 방문하지 않은 값이라면
                    q.append([nx, ny])#9)큐에 좌표를 추가
                    visited[nx][ny] = 1 #10)해당좌표 방문표시

#1)입력
n = int(input())
board = [list(map(str, input())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
q = deque()

cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0: #2)방문 전이면
            bfs(i, j) #3)해당 좌표를 전달
            cnt += 1 #11)bfs에서 한 구역을 돌았으니, cnt+1
print(cnt, end=' ')

#적색과 녹색이 동일하도록 변경
for i in range(n):
    for j in range(n):
        if board[i][j] == 'R':
            board[i][j] = 'G'
visited = [[0]*n for _ in range(n)]

cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            cnt += 1
print(cnt)
```

- DFS 코드

```python
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
```

## 3. 어려웠던 점

- 그림이라는 문제랑 비슷!
- dfs로 풀 경우, recursion limit이 설정이 필요
