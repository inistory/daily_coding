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
        v = queue.popleft()
        for i in graph[v]: #해당 노드의 인접 노드들 확인
            if not visited[i]:#아직 방문하지않은 인접노드들을 
                queue.append(i) #찾는 족족 다 큐에 삽입
                visited[i] = True #방문처리
                distance[i] += distance[v]+ 1 

    exist  = False
    for i, c in enumerate(distance):
        if c == K:
            print(i)
            exist = True 
    if exist == False:
            print(-1)
           
bfs(graph,X,visited,distance)
