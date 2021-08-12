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
