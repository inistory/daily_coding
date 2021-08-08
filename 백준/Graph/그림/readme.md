## 1. 문제 설명

[문제 링크](acmicpc.net/problem/1926)

- 첫째 줄: 도화지의 세로크기
- 둘째 줄: 도화지의 가로크기
- 그 아래 줄: 도화지와 그림 정보
- return : 첫째 줄에는 그림의 개수, 둘째 줄에는 그 중 가장 넓은 그림의 넓이 출력

## 2. 코드

```python
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

```

## 3. 어려웠던 점

- 주어진 2차원 배열에서 여러개가 모여있을 때 하나의 그림으로 간주하는 조건을 어떻게 세우는지
- 넓이는 어떻게 구하는지
- 이걸 bfs를 써서 어떻게 푸는지
- bfs로 푼다면 이건 양방향그래프라고 생각하고 풀어야하는지
- 방식은 이해갔는데, 위 아래 오른쪽 왼쪽을 확인하고 1씩늘리면, 넓이는 가로\*세로 인데 count+1만으로 어떻게 넓이가 구해는건지
