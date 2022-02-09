from collections import deque
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True #현재 노드 방문처리
    while queue:
        v = queue.poplieft()
        print(v, end='')
        
        for i in graph[v]: #해당 노드의 인접 노드들 확인
            if not visited[i]:#아직 방문하지않은 인접노드들을 
                queue.append(i) #찾는 족족 다 큐에 삽입
                visited[i] = True #방문처리


graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False]*9
bfs(graph,1,visited)