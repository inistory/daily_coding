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