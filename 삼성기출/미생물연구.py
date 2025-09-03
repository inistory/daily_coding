from collections import deque

# 미생물 연구 시뮬레이션
# 1. 입력 및 초기화
N, Q = map(int, input().split())
grid = [[0]*N for _ in range(N)] # 0=빈칸, >0=미생물 그룹ID
next_group_id = 0 # 새 그룹에 부여할 ID
DIR = [(1,0), (-1,0), (0,1), (0,-1)] # 상하좌우

# 2. 연결된 미생물 그룹 찾기 (BFS)
def bfs(sr, sc, group_id, visited):
    queue = deque([(sr, sc)])
    visited[sr][sc] = True
    cells = [(sr, sc)]
    minr = maxr = sr
    minc = maxc = sc
    while queue:
        r, c = queue.popleft()
        for dr, dc in DIR:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and grid[nr][nc] == group_id:
                visited[nr][nc] = True
                queue.append((nr, nc))
                cells.append((nr, nc))
                minr = min(minr, nr)
                maxr = max(maxr, nr)
                minc = min(minc, nc)
                maxc = max(maxc, nc)
    return cells, (minr, minc, maxr, maxc)

# 3. 살아남은 그룹과 소멸 그룹 판정
#    - 같은 그룹ID가 여러 덩어리로 분리되면 소멸 처리
#    - 살아남은 그룹 정보 반환

def get_alive_groups_and_mark_dead():
    visited = [[False]*N for _ in range(N)]
    seen_once = set()
    dead = set()
    groups = []
    for r in range(N):
        for c in range(N):
            group_id = grid[r][c]
            if group_id == 0 or visited[r][c]:
                continue
            cells, bbox = bfs(r, c, group_id, visited)
            if group_id in dead:
                continue
            if group_id in seen_once:
                dead.add(group_id)
            else:
                seen_once.add(group_id)
                groups.append({
                    "id": group_id,
                    "cells": cells,
                    "bbox": bbox,
                    "size": len(cells)
                })
    groups = [g for g in groups if g["id"] not in dead]
    return groups, dead

# 4. 새 용기에 그룹 배치 시도
#    - 모양 그대로 빈 공간에 배치
#    - 배치 실패 시 소멸

def place_group_in_new_grid(cells, bbox, new_grid, group_id):
    minr, minc, maxr, maxc = bbox
    height = maxr - minr + 1
    width = maxc - minc + 1
    rel_cells = [(r - minr, c - minc) for (r, c) in cells]
    for y in range(0, N - height + 1):
        for x in range(0, N - width + 1):
            can_place = True
            for rr, cc in rel_cells:
                if new_grid[y+rr][x+cc] != 0:
                    can_place = False
                    break
            if can_place:
                for rr, cc in rel_cells:
                    new_grid[y+rr][x+cc] = group_id
                return True
    return False

# 5. 점수 계산
#    - 서로 다른 그룹이 상하좌우로 맞닿아 있으면 두 그룹 크기 곱만큼 점수

def calculate_score(curr_grid):
    area = {}
    for r in range(N):
        for c in range(N):
            group_id = curr_grid[r][c]
            if group_id:
                area[group_id] = area.get(group_id, 0) + 1
    adj = set()
    for r in range(N):
        for c in range(N):
            a = curr_grid[r][c]
            if a == 0:
                continue
            for dr, dc in DIR:
                nr, nc = r+dr, c+dc
                if 0 <= nr < N and 0 <= nc < N:
                    b = curr_grid[nr][nc]
                    if b and b != a:
                        pair = (a, b) if a < b else (b, a)
                        adj.add(pair)
    total = 0
    for a, b in adj:
        total += area[a] * area[b]
    return total

# 6. 시뮬레이션 메인 루프
for _ in range(Q):
    # 미생물 투입
    r1, c1, r2, c2 = map(int, input().split())
    next_group_id += 1
    for r in range(r1, r2):
        for c in range(c1, c2):
            grid[r][c] = next_group_id
    # 그룹 재구성 및 소멸 판정
    groups, dead = get_alive_groups_and_mark_dead()
    # 크기 내림차순(큰순), ID 오름차순 정렬(빠른순)
    groups.sort(key=lambda x: (-x["size"], x["id"]))
    # 새 용기 준비
    new_grid = [[0]*N for _ in range(N)]
    # 그룹 배치
    for group in groups:
        place_group_in_new_grid(group["cells"], group["bbox"], new_grid, group["id"])
    grid = new_grid
    # 점수 출력
    print(calculate_score(grid))
