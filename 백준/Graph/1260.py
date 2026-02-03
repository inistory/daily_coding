"""
- 2026-02-03
- 문제:
    정점의 개수 N, 간선의 개수 M, 탐색 시작 정점 V와
    간선 정보가 주어질 때,
    DFS 탐색 결과와 BFS 탐색 결과를 각각 출력한다.
    단, 방문할 수 있는 정점이 여러 개인 경우
    정점 번호가 작은 것부터 방문한다.

- 접근법:
    1) 인접 리스트를 이용해 그래프를 구성한다.
       - graph[i]에는 i번 정점과 연결된 모든 정점 번호를 저장
       - 무방향 그래프이므로 양방향으로 간선을 추가

    2) 각 정점의 인접 리스트를 오름차순 정렬한다.
       - DFS, BFS 모두에서 번호가 작은 정점부터 탐색하기 위함

    3) DFS
       - 재귀를 이용한 깊이 우선 탐색
       - 현재 정점을 방문 처리 후 출력
       - 인접한 정점 중 아직 방문하지 않은 정점으로 재귀 호출

    4) BFS
       - 큐(deque)를 이용한 너비 우선 탐색
       - 시작 정점을 큐에 넣고 방문 처리
       - 큐에서 하나씩 꺼내며 인접 정점을 순서대로 방문

    5) DFS와 BFS는 방문 배열을 공유할 수 없으므로
       BFS 실행 전에 visited 배열을 초기화한다.
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
