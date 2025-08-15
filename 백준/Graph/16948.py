from collections import deque
import sys
input = sys.stdin.readline

N = int(input().strip())
r1, c1, r2, c2 = map(int, input().split())

visited = [[-1] * N for _ in range(N)]#(r1,c1)에서 (x,y)까지 이동하는 데 필요한 최소 이동 횟수
q = deque([(r1, c1)])
visited[r1][c1] = 0#0번이동(시작점이니까)

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

while q:
    x, y = q.popleft()
    if x == r2 and y == c2:
        break
    for k in range(6):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))

print(visited[r2][c2])
