from collections import deque
import sys

input = sys.stdin.readline

n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

DIRS = [(-1,0), (1,0), (0,-1), (0,1)]

def bfs(sx, sy, visited):
    q = deque([(sx, sy)])
    visited[sx][sy] = True

    cells = [(sx, sy)]
    total = arr[sx][sy]

    while q:
        x, y = q.popleft()
        for dx, dy in DIRS:
            nx, ny = x + dx, y + dy

            # 필터성 조건 → continue로 명확하게 스킵
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if visited[nx][ny]:
                continue

            diff = abs(arr[x][y] - arr[nx][ny])
            if l <= diff <= r:
                visited[nx][ny] = True
                q.append((nx, ny))
                cells.append((nx, ny))
                total += arr[nx][ny]

    return cells, total


days = 0

while True:
    visited = [[False] * n for _ in range(n)]
    moved = False

    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue  # 하루에 여러 번 연합 시작하지 않게

            cells, total = bfs(i, j, visited)

            if len(cells) > 1:
                moved = True
                avg = total // len(cells)
                for x, y in cells:
                    arr[x][y] = avg

    if not moved:
        break
    days += 1

print(days)