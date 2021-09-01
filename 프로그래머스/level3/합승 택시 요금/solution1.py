INF = 40000000
def floyd(dist, n):
    for k in range(n): #경유지노드
        for i in range(n): #출발점
            for j in range(n): #도착점
                if dist[i][k] + dist[k][j] < dist[i][j]: #i에서 j로 가는데 k를 경유
                    dist[i][j] = dist[i][k] + dist[k][j]
                    
def solution(n,s,a,b,fares):
    dist = [[INF for _ in range(n)]for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
        
    for edge in fares:
        dist[edge[0]-1][edge[1]-1] = edge[2] #인덱스를 0부터 사용하기 위해서 1을 빼서 사용, 비용을 넣는다
        dist[edge[1]-1][edge[0]-1] = edge[2] #양방향
        
        
    floyd(dist,n)
    s-=1
    a-=1
    b-=1
    answer = INF
    for k in range(n):
        answer = min(answer,dist[s][k] + dist[k][a] + dist[k][b])
    return answer
