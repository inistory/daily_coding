def dfs (graph, v, visited):
    #현재 노드를 방문 처리
    visited[v] = True
    print(v, end='')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]: #정점의 인접노드들의 확인
        if not visited[i]: #인접노드들 중에 방문하지 않은 노드가 있다면
            dfs(graph, i, visited) #방문처리


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
dfs(graph,1,visited)
