def solution(n, computers):
    answer = 0
    bfs = []
    visited = [0]*n

    while 0 in visited:	# visited 리스트의 모든 값에 방문 표시가 되어있을 때까지 반복
        bfs.append(visited.index(0))#방문하지 않은 노드를 찾아서
        print(bfs)
        while bfs:
            node = bfs.pop(0) # 큐의 앞에서부터 노드(인덱스) 꺼내기
            visited[node] = 1 #방문표시
            for i in range(n): # 꺼낸 노드의 인접 노드를 방문하기 위한 반복문 수행
                if visited[i] == 0 and computers[node][i] == 1:
                    bfs.append(i)
        answer += 1
    print(bfs)
    return answer