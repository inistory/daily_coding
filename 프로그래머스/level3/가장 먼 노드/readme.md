## 1. 문제 설명

[문제 링크](https://www.acmicpc.net/problem/49189)

- n : 노드의 갯수
- vertex : 간선에 대한 정보가 담긴 2차원 배열
- return : 1번 노드로부터 가장 멀리 떨어진 노드 (최단경로로 이동했을 때 간선의 개수가 가장 많은 노드) 의 갯수

## 2. 코드

```python
from collections import deque

def bfs(v,adj_list,visited):
    count = 0
    q = deque([[v, count]])

    while q: #큐에 아무것도 없을 때까지 반복
        value = q.popleft()
        v = value[0]
        count = value[1]

        if visited[v] == -1:
            visited[v] = count #첫번째 노드는 count = 0
            count+=1 #그 다음 노드에는 거리 1추가

            for node in adj_list[v]: #인접 노드 정보를 count와 함께 큐에 넣는다
                q.append([node, count])

def solution(n, edge):
    answer = 0
    visited = [-1] * (n+1) #방문하지 않는 노드는 -1로 표시하여 bfs시 조건으로 사용

    #인접리스트 만들기
    adj_list = [[] for _ in range(n+1)]
    for e in edge:
        adj_list[e[0]].append(e[1])
        adj_list[e[1]].append(e[0])

    bfs(1,adj_list,visited)

    for visit in visited:
        if visit == max(visited):
            answer+=1
    return answer

```

## 3. 어려웠던 점

- visited에 바로 거리를 입력하면 해결되는걸 다른 변수로 해결하려했었다.
- bfs 코드를 외워놓아야겠다
- deque 를 사용하면 그냥 리스트를 사용할 때보다 pop할 때 효율적이다.
