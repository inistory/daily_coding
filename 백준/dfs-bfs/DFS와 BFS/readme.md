## 1. 문제 설명

[문제 링크](https://www.acmicpc.net/problem/1260)

- 입력
  - 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
  - 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다.
- 출력 : 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

## 2. 코드

solution1.py

```python
# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline
from collections import deque

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

def dfs(graph, v, visited):
    #현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]: #정점의 인접노드들의 확인
        if not visited[i]: #인접노드들 중에 방문하지 않은 노드가 있다면
            dfs(graph, i, visited) #방문처리


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True #현재 노드 방문처리
    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]: #해당 노드의 인접 노드들 확인
            if not visited[i]:#아직 방문하지않은 인접노드들을
                queue.append(i) #찾는 족족 다 큐에 삽입
                visited[i] = True #방문처리

visited = [False]*(N+1)
dfs(graph, V, visited)
visited = [False]*(N+1)
print()
bfs(graph, V, visited)
```

## 3. 회고

- dfs, bfs 기초 문제로 풀기 좋았다.
- graph정보를 입력 받은 뒤 sort()를 꼭 해주어야한다.(정점 번호가 작은 것을 먼저 방문한다는 조건이 존재한다.)
- visited = [False]\*(N+1)를 통해 visited 초기화한 후 bfs를 수행해야한다.
- print()를 통해 dfs 후에 줄바꿈을 해줘야한다. 이걸 안해서 출력 형식이 잘못되었다고 떴었다 ㅠㅠ
