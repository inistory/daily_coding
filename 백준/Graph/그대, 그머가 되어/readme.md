## 1. 문제 설명

[문제 링크](acmicpc.net/problem/14496)

- 첫째 줄 : 머호가 바꾸려 하는 문자 a와 b
- 둘째 줄 : 전체 문자의 수 N과 치환 가능한 문자쌍의 수 M
- 이 후: M개의 줄에 걸쳐 치환 가능한 문자쌍

## 2. 코드

```python
#dijkstra
import sys, heapq
INF = int(1e9)
a,b = map(int,sys.stdin.readline().split())
n,m = map(int,sys.stdin.readline().split())

board = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int,sys.stdin.readline().split())
    board[x].append(y)
    board[y].append(x)

dist_table = [INF]*(n+1) #최단 거리 테이블
dist_table[a] = 0
q = []
heapq.heappush(q, (0,a))

while q: #큐가 비어있지 않다면
    #최단거리가 짧은 노드에 대한 정보를 꺼내기
    dist, cur_node = heapq.heappop(q)
    #현재 노드가 이미 처리된 적이 있는 노드라면 무시
    if dist_table[cur_node] < dist:
        continue
    #현재 노드와 연결된 인접한 노드들을 확인
    for next in board[cur_node]:
        #현재 가중치가 저장되어있는 가중치보다 작다면 현재 가중치 넣어줌
        if dist_table[next] > dist+1:
            dist_table[next] = dist+1
            heapq.heappush(q, (dist+1,next))

#모든 노드로 가기 위한 최단 거리를 출력
if dist_table[b] == INF:
    print(-1)
else:
    print(dist_table[b])

```

```python
#BFS
import sys
from collections import deque
INF = int(1e9)
a,b = map(int,sys.stdin.readline().split())
n,m = map(int,sys.stdin.readline().split())

board = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int,sys.stdin.readline().split())
    board[x].append(y)
    board[y].append(x)

count = INF
visited = [False]*(n+1) #최단 거리 테이블
visited[a] = True
q = deque([(0,a)])

while q: #큐가 비어있지 않다면
    dist, cur_node = q.popleft()
    if cur_node == b:
        count = min(count,dist)
    for next in board[cur_node]:
        if not visited[next]: #방문하지 않았다면
            visited[next] = True #방문상태로 바꿔줌
            q.append((dist+1,next))

if count == INF:
    print(-1)
else:
    print(count)

```

## 3. 어려웠던 점

- 우선순위 큐를 사용한다는 점
- 다익스트라 알고리즘의 활용

`
