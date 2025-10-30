import sys
import heapq

input = sys.stdin.readline
INF = 10**18

v, e = map(int, input().split())     # 정점 수 V, 간선 수 E
start = int(input())         # 시작 정점 K

# 인접 리스트: graph[u] = [(v, w), ...]  (u -> v, 가중치 w)
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))          # 방향 그래프이므로 a -> b만 추가

# 최단거리 배열
dist = [INF] * (v + 1)
dist[start] = 0

# 우선순위 큐(힙): (현재까지의 거리, 정점)
pq = [(0, start)]

while pq:
    d, u = heapq.heappop(pq)

    # 힙에서 꺼낸 정보가 최신이 아니면 스킵 (중복/오래된 상태 제거)
    # d(옛날거리), dist[u](최신최단거리)
    # 이 둘이 다르다면 이미 더 짧은 길을 찾은 정점이므로 패스
    if d != dist[u]:
        continue

    # u에서 나가는 모든 간선 이완(어떤경로를 통해서 더 짧게갈수있다면 거리값을갱신)
    for nv, w in graph[u]:
        nd = d + w
        if nd < dist[nv]:
            dist[nv] = nd
            heapq.heappush(pq, (nd, nv))

# 출력: 1번 정점부터 V번 정점까지
out = []
for i in range(1, v + 1):
    if dist[i] == INF:
        out.append("INF")
    else:
        out.append(str(dist[i]))
print("\n".join(out))
