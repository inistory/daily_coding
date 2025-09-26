# -*- coding: utf-8 -*-
from collections import deque

# 이동 우선순위: 상, 하, 좌, 우
TIE_DIR = [(-1,0), (1,0), (0,-1), (0,1)]

def oob(r, c, n):
    return not (0 <= r < n and 0 <= c < n)

def manhattan(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)

def move_people(people, grid, ex, ey):
    """맨해튼 거리 감소 방향으로 1칸 이동 (상/하 우선 → 좌/우), 벽(>0) 불가."""
    n = len(grid)
    moved_cnt = 0
    new_people = []
    for r, c in people:
        if (r, c) == (ex, ey):
            # 이미 도착한 사람은 목록에 남아있지 않도록 관리하지만 방어
            continue
        base = manhattan(r, c, ex, ey)
        moved = False
        for dr, dc in TIE_DIR:
            nr, nc = r + dr, c + dc
            if oob(nr, nc, n):            continue
            if grid[nr][nc] > 0:          continue  # 벽으로 이동 불가
            if manhattan(nr, nc, ex, ey) < base:
                r, c = nr, nc
                moved = True
                moved_cnt += 1
                break
        # 출구에 도착하지 않은 사람만 유지
        if (r, c) != (ex, ey):
            new_people.append((r, c))
    return new_people, moved_cnt

def find_min_square(people, ex, ey, n):
    """출구와 참가자 ≥1명을 포함하는 최소 정사각형 (크기→행→열 우선)."""
    if not people:
        return None
    for sz in range(2, n+1):
        for x0 in range(0, n - sz + 1):
            for y0 in range(0, n - sz + 1):
                if not (x0 <= ex < x0+sz and y0 <= ey < y0+sz):
                    continue
                # 내부에 참가자 1명 이상?
                inside = False
                for pr, pc in people:
                    if x0 <= pr < x0+sz and y0 <= pc < y0+sz:
                        inside = True
                        break
                if inside:
                    return (x0, y0, sz)
    return None

def rotate_cw_square(grid, people, ex, ey, square):
    """정사각형을 시계 90° 회전. 그 내부 벽 내구도 1 감소. 사람/출구도 함께 회전."""
    x0, y0, sz = square
    n = len(grid)
    old = [row[:] for row in grid]

    # 1) 그리드 회전 (시계 90°)
    for i in range(sz):
        for j in range(sz):
            grid[x0 + j][y0 + (sz - 1 - i)] = old[x0 + i][y0 + j]

    # 2) 회전된 정사각형 내부 벽 내구도 감소(>0만)
    for i in range(x0, x0+sz):
        for j in range(y0, y0+sz):
            if grid[i][j] > 0:
                grid[i][j] -= 1

    # 3) 좌표 회전 (사람/출구)
    def rot_pos(r, c):
        i, j = r - x0, c - y0
        return (x0 + j, y0 + (sz - 1 - i))

    new_people = []
    for r, c in people:
        if x0 <= r < x0+sz and y0 <= c < y0+sz:
            nr, nc = rot_pos(r, c)
            new_people.append((nr, nc))
        else:
            new_people.append((r, c))

    if x0 <= ex < x0+sz and y0 <= ey < y0+sz:
        ex, ey = rot_pos(ex, ey)

    return grid, new_people, ex, ey

##main
n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

people = []
for _ in range(m):
    r, c = map(int, input().split())
    people.append((r-1, c-1))  # 0-index

ex, ey = map(int, input().split())
ex, ey = ex-1, ey-1            # 0-index

total_move = 0
for _ in range(k):
    if not people:
        break

    # 1) 참가자 이동(동시): 맨해튼 감소 + 상/하 → 좌/우
    people, moved = move_people(people, grid, ex, ey)
    total_move += moved
    if not people:
        break

    # 2) 회전(최소 정사각형 → 시계90° → 내구도-1, 사람/출구 동반 회전)
    sq = find_min_square(people, ex, ey, n)
    if sq is not None:
        grid, people, ex, ey = rotate_cw_square(grid, people, ex, ey, sq)

print(total_move)
print(ex+1, ey+1)
