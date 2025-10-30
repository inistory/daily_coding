import sys
from collections import deque

input = sys.stdin.readline

# 입력
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)] #인접리스트
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)  # 단방향 그래프

# 거리 배열 초기화 (-1: 미방문)
dist = [-1] * (n + 1)
dist[x] = 0

# BFS
q = deque([x])
while q:
    cur = q.popleft()
    for nxt in graph[cur]:
        if dist[nxt] == -1:
            dist[nxt] = dist[cur] + 1
            q.append(nxt)

# 거리 k인 도시 출력 (오름차순)
found = False
for city in range(1, n + 1):
    if dist[city] == k:
        print(city)
        found = True

if not found:
    print(-1)
