# Track B: 층 BFS + 동시 이동(메이즈 러너 계열) 스켈레톤
# 입력 포맷: N M -> N줄의 문자 격자('#'=벽, '.'=빈칸, 'S'=시작 여러 개 가능)
# 예시 실행: python trackB.py < inputs/B1.txt

from collections import deque

DIR4 = [(-1,0),(0,1),(1,0),(0,-1)]#상,우,하,좌

#inthebound
def inb(i, j, n, m):
    return 0 <= i < n and 0 <= j < m

def find_starts(grid, ch,n,m):
    starts = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == ch:
                starts.append((i, j))
    return starts

def layer_bfs(starts, is_block, n, m):
    q = deque(starts)
    dist = [[-1]*m for _ in range(n)]#최단턴수를 저장
    for i, j in starts: #start는 출발지점이니까 0턴으로 설정
        dist[i][j] = 0

    while q:
        for _ in range(len(q)):  # 지금 큐에 있는 애들 = 같은 시간층(같은 턴)
            i, j = q.popleft()
            for di, dj in DIR4:
                ni, nj = i + di, j + dj
                if not inb(ni, nj, n, m):
                    continue
                if is_block(ni, nj) or dist[ni][nj] != -1:
                    continue
                # 격자를 벗어나지않고, 블럭(#)이없으며,미방문칸이라면
                dist[ni][nj] = dist[i][j] + 1 #최대거리를 업데이트
                q.append((ni, nj)) #큐에 추가
    return dist

#main
n, m = map(int, input().split())#행 개수, 열 개수
grid = [list(input().strip()) for _ in range(n)] #grid만들기

#그 칸이 막힌 칸인지 판단하는 함수
#'#'면 True(벽이라못지나감),그 외면 False(지나갈 수 있음)
def is_block(i, j):
    return grid[i][j] == '#'

starts = find_starts(grid, 'S',n,m) #시작 좌표
dist = layer_bfs(starts, is_block, n, m)

# TODO: 문제에 맞는 후처리(예: 'E'까지 최단거리, 가장 가까운 대상 등)
# 일단은 도달 가능한 칸들의 최대 거리만 출력
ans = 0
#BFS로 만든 거리맵에서 도달 가능한 칸들 중 가장 먼 거리 출력(최대턴수)
for i in range(n):
    for j in range(m):
        if dist[i][j] > ans:
            ans = dist[i][j]
print(ans)

