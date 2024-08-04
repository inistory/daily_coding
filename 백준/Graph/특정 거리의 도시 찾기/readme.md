## 1. 문제 설명

[문제 링크](https://www.acmicpc.net/problem/18352)

- 입력
  - 첫째 줄에 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
  - 둘째 줄부터 M개의 줄에 걸쳐서 두 개의 자연수 A, B가 공백을 기준으로 구분되어 주어짐, 이는 A번 도시에서 B번 도시로 이동하는 단방향 도로가 존재한다는 의미
- 출력 : [3,4,2,1,5] 실패율이 높은 스테이지순으로 출력, 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1

## 2. 코드

solution1.py

```python
# -*- coding: utf-8 -*-
#노드, 간선 graph 만들기
from collections import deque
import sys
input = sys.stdin.readline
N,M,K,X = map(int, input().split())
graph = [[] for _ in range(N+1)] #각 노드(0~N)개 별로 리스트가 존재하도록 초기화
distance = [0 for _ in range(N+1)]
visited = [False]*(N+1)
#노드 연결정보를 참고하여 graph list에 추가
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

#출발노드 X로부터 각 노드까지 거리를 계산하고 거리가 K인 노드만 출력
def bfs(graph, start, visited, distance):
    queue = deque([start])
    visited[start] = True #현재 노드 방문처리
    distance[start] = 0
    while queue:
        v = queue.popleft() #현재노드
        for i in graph[v]: #해당 노드의 인접 노드들 확인
            if not visited[i]:#아직 방문하지않은 인접노드들을
                queue.append(i) #찾는 족족 다 큐에 삽입
                visited[i] = True #방문처리
                distance[i] += distance[v]+ 1#

    exist  = False
    for i, c in enumerate(distance):
        if c == K:
            print(i)
            exist = True
    if exist == False:
            print(-1)

bfs(graph,X,visited,distance)

```

## 3. 회고

- 처음에 풀 때 런타임 에러(IndexError)가 났다.
- visited = [False]\*(N+1) 로 해야하는데, visited = [False]\*9 로 되어 있었다. ㅠㅠ
- bfs 를 통해 아직 방문하지 않은 인접노드 i를 찾았을 때, 방문처리를 해주는 부분에서 이전 노드까지의 거리를 나타내는 distance[v]에 +1 을 해서 새롭게 방문하는 노드까지의 거리(distance[i])에 저장해준다.
