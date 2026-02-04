"""
- 2026-02-04
- 문제:
    - 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다.
    - 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때
    - 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성
- 접근법:
    - bfs로 1인 것만 찾아서 넣기
    - (n,m)위치에서 종료
    - 큐에 이동거리 넣어서 추적
"""

from collections import deque

N, M = map(int, input().split())
graph = [list(input().strip()) for _ in range(N)]

q = deque([(0, 0, 1)])
visited = [[False]*M for _ in range(N)]
visited[0][0] = True

dx = [0,0,-1,1]
dy = [1,-1,0,0]

while q:
    x, y, d = q.popleft()

    if x == N-1 and y == M-1:
        print(d)
        break

    for k in range(4):
        a, b = x + dx[k], y + dy[k]
        if not (0 <= a < N and 0 <= b < M):
            continue
        if graph[a][b] == '1' and not visited[a][b]:
            visited[a][b] = True
            q.append((a, b, d + 1))
