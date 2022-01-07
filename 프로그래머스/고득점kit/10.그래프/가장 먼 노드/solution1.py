from collections import deque

def bfs(v,adj_list,visited):
    count = 0
    q = deque([[v, count]]) 
    
    while q: #큐에 아무것도 없을 때까지 반복
        v, count = q.popleft() 
        
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
    
    