#경로 찾기

from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 결과를 저장할 visited 행렬 초기화 (모든 값 0)
visited = [[0]*n for _ in range(n)]

# BFS 함수 정의: 시작 정점 x로부터 도달 가능한 정점을 탐색
def bfs(x):
    queue = deque()
    queue.append(x)  # 시작 정점을 큐에 추가

    # 현재 BFS에서 방문한 정점을 체크하기 위한 리스트
    check = [0 for _ in range(n)]

    while queue:
        q = queue.popleft()

        for i in range(n):
            # q → i로 가는 간선이 있고, 아직 방문하지 않았다면
            if check[i] == 0 and graph[q][i] == 1:
                queue.append(i)     # 다음 탐색 대상으로 추가
                check[i] = 1        # 방문 표시
                visited[x][i] = 1   # x → i 경로 존재함을 표시

# 모든 정점에서 BFS를 수행해 도달 가능한 정점 확인
for i in range(n):
    bfs(i)

# 최종 결과 출력 (경로 존재 여부를 인접 행렬 형태로 출력)
for i in visited:
    print(*i)
