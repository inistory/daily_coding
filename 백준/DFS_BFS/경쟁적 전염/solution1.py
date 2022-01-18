# -*- coding: utf-8 -*-
from collections import deque
import sys
input = sys.stdin.readline

N,K = map(int, input().split())
graph = []
data = [] # 바이러스종류 저장
for i in range(N):
    graph.append(list(map(int, input().split())))
    for j in range(N):
        #해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] !=0:
            #바이러스종류, 초, 위치 x, 위치 y
            data.append((graph[i][j],0,i,j))

data.sort()

#ex1 : deque([(1, 0, 0, 0), (2, 0, 0, 2), (3, 0, 2, 0)])
q = deque(data)

target_s, target_x, target_y = map(int, input().split()) #초, 위치 x, 위치 y

#상하좌우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

while q:
    virus, s, x, y = q.popleft()
    #s초가 지나거나, 큐가 빌때까지 반복
    if s == target_s:
        break
    #현재 노드에서 4가지 위치를 각각 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        #해당 위치로 이동할 수 있는 경우
        if 0 <= nx and nx < N and 0 <=ny  and ny < N:
            #아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s+1, nx,ny))

print(graph[target_x -1][target_y -1])