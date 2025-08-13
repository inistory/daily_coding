from collections import deque

# 0. 입력 및 초기화
N, Q = map(int, input().split())
grid = [[0]*N for _ in range(N)]#0=빈칸, >0=미생물ID
next_id = 0 #투입할 때마다 새ID를 1,2,3 순서로 부여

DIRS = [(1,0), (-1,0), (0,1), (0,-1)] #상하좌우 탐색

#특정 좌표에서 시작해서, 같은 id로 연결된 한 덩어리(컴포넌트)를 BFS로 찾아내고
#그 좌표 목록과 바운딩 박스를 반환하는 함수
def bfs_component(sr, sc, idv, visited):#BFS시작좌표, 찾고자하는 미생물ID, BFS중에 이미 방문한 칸을 표시하는 배열
    q = deque([(sr, sc)]) #시작점을 큐에 넣고
    visited[sr][sc] = True #방문표시
    cells = [(sr, sc)] #cells에 시작점 기록
    minr = maxr = sr #시작점을 기준으로 초기화
    minc = maxc = sc
    while q:#BFS로 연결된 같은 idv값만 탐색
        r, c = q.popleft() #큐에서 한 칸 꺼내서
        for dr, dc in DIRS: #상하좌우 탐색
            nr, nc = r+dr, c+dc
            #범위 안이고, 미방문이며, 같은 id면
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and grid[nr][nc] == idv:
                visited[nr][nc] = True #방문표시하고
                q.append((nr, nc)) #큐에넣기
                cells.append((nr, nc))#cells에 추가
                #바운딩박스범위갱신
                if nr < minr: minr = nr
                if nr > maxr: maxr = nr
                if nc < minc: minc = nc
                if nc > maxc: maxc = nc
    #한 컴포넌트를 구성하는 모든 좌표 목록, 한 컴포넌트를 덮는 최소 직사각형 경계값
    return cells, (minr, minc, maxr, maxc)

#grid에서 덩어리들을 전부 재구성
#투입 후 격자를 전체 훝어 미생물무리(컴포넌트)로 목록화하고,
#같은 id가 둘이상 컴포넌트로 쪼개졌으면 소멸
def rebuild_components_and_mark_dead():
    visited = [[False]*N for _ in range(N)]#BFS탐색 중 본적있는칸인지 표시
    seen_once = set()#이미 한 번 등장한 ID를 기록하는 집합
    dead = set()#같은 ID가 두 번째 덩어리로 등장한 경우 넣는 집합
    comps = []#살아있는 무리의 정보 목록, 각 원소구조: [{id, cells, bbox, size}, ...]
    
    #모든 (r,c)칸을 훑기
    for r in range(N):
        for c in range(N):
            idv = grid[r][c]#id값
            if idv == 0 or visited[r][c]:#빈칸이거나 이미 방문했으면
                continue#건너뜀
            #visited[r][c]가 0이 아니고 미방문이면 bfs_component로 그 ID의 한 컴포넌트를 뽑아옴
            #이 칸이 시작점이 되어 같은 ID로 연결된 한 컴포넌트를 BFS로 찾아냄
            #cells: 무리를 이루는 모든 칸 좌표 목록
            #bbox: 그 무리의 바운딩박스 (minr, minc, maxr, maxc)
            cells, bbox = bfs_component(r, c, idv, visited)
            if idv in dead:#이미 dead에 있는 ID라면 무시
                continue
            if idv in seen_once: #seen_once에 이미 ID가 있다면
                dead.add(idv)  #그 ID는 dead로 기록(분리 소멸)
            else:#처음보는 ID라면
                seen_once.add(idv)#seen_once기록
                comps.append({"id": idv, "cells": cells, "bbox": bbox, "size": len(cells)})#comps에 무리정보 추가
    # dead 처리: comps에서 제거
    comps = [comp for comp in comps if comp["id"] not in dead]
    return comps, dead

#한 미생물 무리를 새 배양기(new_grid)에 모양 그대로 옮겨 담는 함수
#shape_cells: 이 무리를 이루는 모든 칸 좌표 목록
#bbox: 무리를 감싸는 최소 직사각형(minr, minc, maxr, maxc)
#new_grid: 비어 있는 새 격자
#idv:이 무리의 id
def try_place(shape_cells, bbox, new_grid, idv):
    (minr, minc, maxr, maxc) = bbox
    h = maxr - minr + 1
    w = maxc - minc + 1
    # 상대좌표로 변환
    #바운딩박스 좌상단을 (0,0)으로 잡고 무리의 칸 좌표를 상대좌표로 변환
    #이렇게하면 어디에 배치하든 모양이 동일하게 유지됨
    rel = [(r - minr, c - minc) for (r,c) in shape_cells]
    # 배치할 위치 탐색
    #x(열) 최소 → y(행) 최소 순서로 배치 가능한 자리 탐색
    #바운딩박스 크기(w,h)가 새 용기 경계를 넘지 않도록 범위 제한
    for x in range(0, N - w + 1):
        for y in range(0, N - h + 1):
            #상대좌표의 각 칸을 실제 배치 위치 (y+rr,x+cc)로 변환
            ok = True
            for rr, cc in rel:
                if new_grid[y+rr][x+cc] != 0:
                    ok = False; break #하나라도 이미 차있으면 ok = False로 중단
            if ok:#새 용기에서 모든 칸이 빈칸(0)이면 배치 가능
                for rr, cc in rel:
                    new_grid[y+rr][x+cc] = idv#가능하면 새 용기 new_grid에 해당 칸을 ID로 채움
                return True #성공했음을 알리기 위해 True 반환
    return False

#현재용기(curr_grid)상태를 보고 점수를 계산하는 함수
#서로 다른 미생물 무리(id)가 상하좌우로 맞닿아 있는 경우에만 점수가 생김
#두 무리 크기의 곱
def score_and_area(curr_grid):
    #id별 크기(area)계산
    #curr_grid 전체를 훑어서
    #idv가 0(빈칸)이 아니면, 해당 id의 크기(칸수)를 area 딕셔너리에 기록
    #area예시: area = {1: 4, 2: 6, 3: 5} %id, id에 해당하는 무리의 칸 개수
    area = {}
    for r in range(N):
        for c in range(N):
            idv = curr_grid[r][c]
            if idv: area[idv] = area.get(idv, 0) + 1
    # 인접한 서로 다른 id쌍 찾기
    adj = set()
    for r in range(N):
        for c in range(N):
            a = curr_grid[r][c]
            if a == 0: continue #a가 0이 아니고
            for dr, dc in DIRS:#상하좌우방향으로 인접한 칸을 확인
                nr, nc = r+dr, c+dc
                if 0 <= nr < N and 0 <= nc < N:
                    b = curr_grid[nr][nc]
                    if b and b != a:#b도 0이 아니고, a,b가 서로 다르면 인접해있는거임
                        #(a,b)쌍을 작은 id로 먼저 정렬해서 adj집합에 추가(중복방지)
                        if a < b: adj.add((a,b))
                        else:     adj.add((b,a))
    total = 0
    #인접 쌍 (a,b)마다 두 무리 크기(area[a], area[b])를 곱해서 더함
    for a,b in adj:#adj예시: {(1,2), (1,3), (2,3)}
        #area에 a가 있으면 값을 가져오고 아니면 0
        total += area.get(a,0) * area.get(b,0)
    return total

for _ in range(Q):#Q라운드 수행
    r1, c1, r2, c2 = map(int, input().split())#미생물을 넣은 직사각형 좌표
    next_id += 1 #미생물 무리의 고유 ID번호를 순서대로 붙이기 위해 쓰는 변수, 1라운드엔 next_id가 1
    # 1) 투입 (반열린 구간):grid에 넣기
    for r in range(r1, r2):
        for c in range(c1, c2):
            grid[r][c] = next_id
    # 1') 컴포넌트 재구축 + 분리 소멸 표시
    # 살아남은 미생물 무리 목록, 소멸한 미생물 목록
    # {
    #     "id": ID번호,
    #     "cells": [(r1,c1), (r2,c2), ...],  # 무리를 이루는 칸들 좌표
    #     "bbox": (minr, minc, maxr, maxc),  # 무리의 바운딩박스
    #     "size": 칸 개수
    # }
    comps, dead = rebuild_components_and_mark_dead()

    # 2) 이동
    # 크기 내림차순, ID 오름차순:"큰 무리부터, 동률이면 작은 ID부터 배치"
    comps.sort(key=lambda x: (-x["size"], x["id"]))
    #새 용기 준비: 완전히 빈 격자를 새 용기로 만듦
    new_grid = [[0]*N for _ in range(N)]
    #무리 배치
    #try_place는 모양을 유지하며 새 용기 안에 충돌 없이 들어갈 수 있는 첫 좌표를 찾아 배치
    #배치성공: new_grid에 해당 물이가 채워짐
    #실패: 못 놓는 무리는 소멸하므로 그냥 넘어감
    for comp in comps:
        # 이미 dead면 스킵 (rebuild에서 제거했으므로 보통 불필요)
        placed = try_place(comp["cells"], comp["bbox"], new_grid, comp["id"])
        # 못 놓으면 증발이므로 무시
    #용기 교체
    grid = new_grid

    # 3) 점수 기록
    print(score_and_area(grid))
