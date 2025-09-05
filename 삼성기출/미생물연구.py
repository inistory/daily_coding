from collections import deque

# 미생물 연구 시뮬레이션
# 1. 입력 및 초기화
N, Q = map(int, input().split())
grid = [[0]*N for _ in range(N)] # 0=빈칸, >0=미생물 그룹ID
next_group_id = 0 # 새 그룹에 부여할 ID
DIR = [(1,0), (-1,0), (0,1), (0,-1)] # 상하좌우

# 4. 연결된 미생물 그룹 찾기 (BFS)
#    -- 특정 위치(sr, sc)에서 시작해서, 같은 미생물 그룹에 속한 모든 칸과 바운딩박스를 너비 우선 탐색(BFS)으로 찾아내는 함수
def bfs(sr, sc, group_id, visited):
    queue = deque([(sr, sc)])#큐에 처음위치 초기화
    visited[sr][sc] = True #처음은 당연히 방문하니까 추가
    cells = [(sr, sc)] #cells에는 같은 그룹 아이디를 가진 위치들 추가
    minr = maxr = sr #minr,maxr 초기화
    minc = maxc = sc #minc,maxc 초기화
    while queue:#큐에 값이 존재할 때
        r, c = queue.popleft()#r,c뽑기
        for dr, dc in DIR: #상하좌우가져오기
            nr, nc = r+dr, c+dc #r,c로부터 상하좌우 값들
            #격자안에 있고, 방문한적이 없으며 group_id가 같으면
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and grid[nr][nc] == group_id:
                visited[nr][nc] = True #방문처리
                queue.append((nr, nc)) #큐에넣기
                cells.append((nr, nc))#같은 group_id를 가진 위치들 추가
                minr = min(minr, nr) #최대최소갑 업데이트
                maxr = max(maxr, nr)
                minc = min(minc, nc)
                maxc = max(maxc, nc)
    return cells, (minr, minc, maxr, maxc) #cells, bbox리턴

# 3. 살아남은 그룹 판정
#    - 같은 그룹ID가 여러 덩어리로 분리되면 소멸 처리
#    - 살아남은 그룹 정보 반환

def find_alive_groups():
    visited = [[False]*N for _ in range(N)]#방문체크
    seen_once = set()#본적있는지체크
    dead = set()#죽은그룹체크
    groups = []#살아있는그룹체크
    
    #모든 격자 위치를 탐색
    for r in range(N):
        for c in range(N):
            group_id = grid[r][c] #해당 격자의 group_id를 추출
            if group_id == 0 or visited[r][c]:#빈칸이거나 방문했으면 탐색 안함
                continue #중단
            cells, bbox = bfs(r, c, group_id, visited) #grid[r][c]와 같은 그룹찾기
            if group_id in dead:#만약 group_id가 죽은그룹에 속한다면
                continue #중단
            if group_id in seen_once:#group_id를 본적이 있다면
                dead.add(group_id)#dead에 group_id를 추가
            else:#아무것에도 해당안된다면(dead에 속하지도 seen_once에 속하지도 않는다면)
                seen_once.add(group_id)#seen_once에 추가
                groups.append({#groups에 id,그룹구성인덱스, 바운딩박스, 사이즈 추가
                    "id": group_id,
                    "cells": cells,
                    "bbox": bbox,
                    "size": len(cells)
                })
    #groups에 있는 group들 중에 id가 죽은 그룹에 속하지 않는것만 추리기
    groups = [g for g in groups if g["id"] not in dead]
    return groups #그룹들별 정보리턴

# 5. 새 용기에 그룹 배치 시도
#    - 모양 그대로 빈 공간에 배치
#    - 배치 실패 시 소멸

def place_to_new_grid(new_grid, cells, bbox, group_id):
    minr, minc, maxr, maxc = bbox #바운딩박스 값 꺼내기
    height = maxr - minr + 1 #그룹의 바운딩박스 세로 크기
    width = maxc - minc + 1 #그룹의 바운딩박스 가로 크기
    rel_cells = [(r - minr, c - minc) for (r, c) in cells]#좌상단(0,0)기준 상대좌표로 표현
    #행 우선(y) → 열 우선(x) 순서로 탐색 (문제 규칙)
    #그룹의 바운딩박스가 바운딩 박스를 안나가게 가능한 시작 좌표를 모두 돌며 시도
    for y in range(0, N - height + 1): #배치할 시작 행 (row,y)
        for x in range(0, N - width + 1):#배치할 시작 열 (col,x)
            can_place = True #현재 위치에 배치가능한지 확인
            for rr, cc in rel_cells:
                #(y+rr, x+cc): 새 격자에서 그룹이 실제로 차지하게 될 좌표
                if new_grid[y+rr][x+cc] != 0:#이미 다른 그룹이 차지한 칸이라면
                    can_place = False #배치 불가능
                    break #배치 멈춤
            if can_place:#배치할 수 있으면
                for rr, cc in rel_cells:# 배치만 하고 함수 종료
                    new_grid[y+rr][x+cc] = group_id
                return

# 5. 점수 계산
#    - 서로 다른 그룹이 상하좌우로 맞닿아 있으면 두 그룹 크기 곱만큼 점수

def calculate_score(curr_grid):
    #1.그룹별로 몇칸 차지하는지 기록
    area = {} #{group_id:칸개수}: 모든 그룹이 몇칸을 차지하는지 기록
    #격자 전체를 훑으면서
    for r in range(N):
        for c in range(N):
            group_id = curr_grid[r][c]#group_id를 보고
            if group_id:#비어있지 않은 칸이면(group_id!=0)
                area[group_id] = area.get(group_id, 0) + 1 #해당 그룹의 id의 count를 증가시킴
    
    #2. 인접한 그룹 쌍 찾기
    adj = set() #인접한 그룹 쌍을 저장하는 집합
    #격자를 다시 훑으면서
    for r in range(N):
        for c in range(N):
            a = curr_grid[r][c]#현재 칸의 group_id
            if a == 0:#현재칸에 group_id가 없다면
                continue
            for dr, dc in DIR:#(r,c)기준 상하좌우 값 가져오기
                nr, nc = r+dr, c+dc
                if 0 <= nr < N and 0 <= nc < N: #격자안에 있는 좌표면
                    b = curr_grid[nr][nc]#그 좌표 넣어서 해당칸을 가져오고
                    if b and b != a:#해당칸에 group_id가 존재하고, 현재값과 같지않으면
                        pair = (a, b) if a < b else (b, a) #맞닿아있음 추가(작은id,큰id):두쌍 인접했을 때 중복저장이 안되도록
                        adj.add(pair)#pair를 adj에 인접한 쌍으로 저장
    total = 0
    for a, b in adj: #인접한 그룹쌍 (a,b)마다
        total += area[a] * area[b] #점수를 더함
    return total

# 2. 시뮬레이션 메인 루프
for _ in range(Q):# 미생물 투입
    r1, c1, r2, c2 = map(int, input().split())#초기 미생물 위치 입력받아서
    next_group_id += 1 #group_id=1부터 기록
    #해당 바운딩 박스 내에 있는 위치들을 가져와서
    for r in range(r1, r2):
        for c in range(c1, c2):
            grid[r][c] = next_group_id #grid에 그룹id를 입력
    groups = find_alive_groups() #살아있는 그룹들의 그룹정보 받기
    # 그룹정보를 크기 내림차순(큰순), ID 오름차순 정렬(빠른순)으로 정렬
    # (새 용기에 배치할 때 순서이기 때문)
    groups.sort(key=lambda x: (-x["size"], x["id"]))
    # 새 용기 준비
    new_grid = [[0]*N for _ in range(N)]
    # 그룹별로 새 용기에 배치
    for group in groups:
        place_to_new_grid(new_grid, group["cells"], group["bbox"], group["id"])
    grid = new_grid #그룹군집을 옮겨담기, 이 과정이 있어야 계속 grid가 업데이트됨
    # 점수 출력
    print(calculate_score(grid))