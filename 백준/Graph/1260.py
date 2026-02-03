"""
- 2026-02-03
- 문제: 정점개수, 간선개수, 탐색 시작 정점번호, 연결정보가 주어질 때, dfs탐색정보와 bfs탐색 정보를 출력
- 접근법:
    1)
"""

from collections import deque

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    graph[i].sort()

visited = [False] * (N + 1)

def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for nxt in graph[v]:
        if not visited[nxt]:
            dfs(nxt)

def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        print(v, end=' ')
        for nxt in graph[v]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)

dfs(V)
print()

visited = [False] * (N + 1)
bfs(V)
