from collections import deque
import heapq

# 상, 하, 좌, 우
DR = [-1, 1, 0, 0]
DC = [0, 0, -1, 1]

# -----------------------------
# 입력
# -----------------------------
N, M = map(int, input().split())
sr, sc, er, ec = map(int, input().split())

line = input().strip()  # m=0이어도 한 줄 읽기
arr = list(map(int, line.split())) if line else []

# 0=도로, 1=마을(벽)
grid = [list(map(int, input().split())) for _ in range(N)]

# 상태
medusa_pos = [sr, sc]#메두사 위치
park_pos = [er, ec]#공원 위치

# 칸별 전사 수
warrior_map = [[0] * N for _ in range(N)]
# 이번 턴 석화된 전사(다음 단계에 복구)
next_warrior_map = [[0] * N for _ in range(N)]
# 전사 큐 (개별 유닛)
warriors = deque()
for i in range(M):
    r, c = arr[2 * i], arr[2 * i + 1]
    warrior_map[r][c] += 1
    warriors.append([r, c])

# 메두사 시야(방향별 보이는 칸을 따로 가록ㅓㅁ)
medusa_area = [[[False] * N for _ in range(N)] for _ in range(4)]


# -----------------------------
# (nr, nc)에서 공원까지 "도로만" 최단거리
# -----------------------------
def road_dist_from(nr, nc):
    if grid[nr][nc] == 1:
        return -1
    if nr == park_pos[0] and nc == park_pos[1]:
        return 0
    pq = []
    heapq.heappush(pq, (0, nr, nc))
    visited = [[False] * N for _ in range(N)]
    visited[nr][nc] = True
    while pq:
        dist, r, c = heapq.heappop(pq)
        if r == park_pos[0] and c == park_pos[1]:
            return dist
        for k in range(4):
            rr, cc = r + DR[k], c + DC[k]
            if 0 <= rr < N and 0 <= cc < N and not visited[rr][cc] and grid[rr][cc] == 0:
                visited[rr][cc] = True
                heapq.heappush(pq, (dist + 1, rr, cc))
    return -1


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# -----------------------------
# 1단계: 메두사 이동
#  - 도로만, 공원까지 최단거리 감소 방향
#  - tie: 방향 인덱스가 작은 순
#  - 경로 없으면 "-1\n", 공원 도착하면 "0\n" 추가 후 False 반환
# -----------------------------
def move_medusa(out_lines, visited):
    pq = []
    for i in range(4):
        nr, nc = medusa_pos[0] + DR[i], medusa_pos[1] + DC[i]
        if not (0 <= nr < N and 0 <= nc < N):
            continue
        if visited[nr][nc] or grid[nr][nc] == 1:
            continue
        dist = road_dist_from(nr, nc)
        if dist == -1:
            continue
        heapq.heappush(pq, (dist, i, nr, nc))

    if not pq:
        out_lines.append("-1\n")
        return False

    _, _, nr, nc = heapq.heappop(pq)
    medusa_pos[0], medusa_pos[1] = nr, nc

    # 공원 도착 즉시 종료
    if medusa_pos[0] == park_pos[0] and medusa_pos[1] == park_pos[1]:
        out_lines.append("0\n")
        return False

    # 메두사가 밟은 칸의 전사 제거
    if warrior_map[nr][nc] > 0:
        size = len(warriors)
        for _ in range(size):
            r, c = warriors.popleft()
            if r == nr and c == nc:
                continue  # 소멸
            warriors.append([r, c])
        warrior_map[nr][nc] = 0

    return True


# -----------------------------
# 2단계: 메두사 시선(90도) + 가림, 석화 수 집계
#  - 반환: (kill_count, best_dir)
#  - medusa_area[best_dir]에 표시, 석화는 next_warrior_map에 잠시 보관
# -----------------------------
def choose_sight_and_petrify():
    best_list = []

    for d in range(4):
        # 초기화
        for r in range(N):
            for c in range(N):
                medusa_area[d][r][c] = False

        # rock: 상/하 → 열 기준, 좌/우 → 행 기준 가림 배열
        rock = [False] * N
        kill_count = 0

        # 1) 정면 직선 표시 + 첫 전사까지 카운트
        for step in range(1, N):
            r = medusa_pos[0] + step * DR[d]
            c = medusa_pos[1] + step * DC[d]
            if r < 0 or r >= N or c < 0 or c >= N:
                break
            medusa_area[d][r][c] = True
            if warrior_map[r][c] > 0:
                if d <= 1:    # 상/하 → 열
                    rock[c] = True
                else:         # 좌/우 → 행
                    rock[r] = True
                kill_count += warrior_map[r][c]
                break

        # 2) 정면을 따라가며 좌/우(또는 상/하) 부채꼴 확장 + 가림
        cur_r, cur_c = medusa_pos[0], medusa_pos[1]
        while 0 <= cur_r < N and 0 <= cur_c < N:
            left_done = False
            right_done = False
            step = 1
            while step <= N and (not left_done or not right_done):
                r = cur_r + (DR[d] * step) if d <= 1 else cur_r
                c = cur_c if d <= 1 else cur_c + (DC[d] * step)

                if d <= 1 and (r < 0 or r >= N):
                    break
                if d > 1 and (c < 0 or c >= N):
                    break

                if d <= 1:
                    # 좌/우로 확장
                    if not left_done and 0 <= (c - step):
                        if rock[c - step]:
                            left_done = True
                        else:
                            medusa_area[d][r][c - step] = True
                            if warrior_map[r][c - step] > 0:
                                rock[c - step] = True
                                left_done = True
                                kill_count += warrior_map[r][c - step]
                    if not right_done and (c + step) < N:
                        if rock[c + step]:
                            right_done = True
                        else:
                            medusa_area[d][r][c + step] = True
                            if warrior_map[r][c + step] > 0:
                                rock[c + step] = True
                                right_done = True
                                kill_count += warrior_map[r][c + step]
                else:
                    # 상/하로 확장
                    if not left_done and 0 <= (r - step):
                        if rock[r - step]:
                            left_done = True
                        else:
                            medusa_area[d][r - step][c] = True
                            if warrior_map[r - step][c] > 0:
                                rock[r - step] = True
                                left_done = True
                                kill_count += warrior_map[r - step][c]
                    if not right_done and (r + step) < N:
                        if rock[r + step]:
                            right_done = True
                        else:
                            medusa_area[d][r + step][c] = True
                            if warrior_map[r + step][c] > 0:
                                rock[r + step] = True
                                right_done = True
                                kill_count += warrior_map[r + step][c]
                step += 1

            cur_r += DR[d]
            cur_c += DC[d]

        best_list.append((kill_count, d))

    # kill 최댓값, 동률이면 방향 인덱스 작은 쪽
    kill_count, best_dir = max(best_list, key=lambda x: (x[0], -0 * x[1]))

    # 석화 칸을 next_warrior_map에 보관하고, warrior_map은 비움
    for r in range(N):
        for c in range(N):
            if medusa_area[best_dir][r][c] and warrior_map[r][c] > 0:
                next_warrior_map[r][c] = warrior_map[r][c]
                warrior_map[r][c] = 0

    return kill_count, best_dir


# -----------------------------
# 3-1단계: 전사 1차 이동 (상,하,좌,우)
#   - 시야 진입 금지
#   - 맨해튼 거리 증가 금지(새 거리 <= 기존 거리)
# -----------------------------
def move_warriors_phase1(sight_dir):
    moved_sum = 0
    size = len(warriors)
    for _ in range(size):
        r, c = warriors.popleft()

        if warrior_map[r][c] == 0:
            continue
        if medusa_pos[0] == r and medusa_pos[1] == c:
            warriors.append([r, c])
            continue

        origin_dist = abs(r - medusa_pos[0]) + abs(c - medusa_pos[1])
        warrior_map[r][c] -= 1

        cand_pq = []
        for j in range(4):
            nr, nc = r + DR[j], c + DC[j]
            if 0 <= nr < N and 0 <= nc < N and not medusa_area[sight_dir][nr][nc]:
                d = abs(nr - medusa_pos[0]) + abs(nc - medusa_pos[1])
                if origin_dist < d:
                    continue  # 증가 금지
                heapq.heappush(cand_pq, (d, j, nr, nc))

        if not cand_pq:
            warrior_map[r][c] += 1
            warriors.append([r, c])
            continue

        _, _, nr, nc = heapq.heappop(cand_pq)
        moved_sum += 1
        warriors.append([nr, nc])
        warrior_map[nr][nc] += 1

    return moved_sum


# -----------------------------
# 3-2단계: 전사 2차 이동 (좌,우,상,하 = 2,3,0,1)
# -----------------------------
def move_warriors_phase2(sight_dir):
    moved_sum = 0
    size = len(warriors)
    for _ in range(size):
        r, c = warriors.popleft()

        if medusa_pos[0] == r and medusa_pos[1] == c:
            warriors.append([r, c])
            continue

        origin_dist = abs(r - medusa_pos[0]) + abs(c - medusa_pos[1])
        warrior_map[r][c] -= 1

        cand_pq = []
        for j in range(2, 6):  # 2,3,0,1 순서
            jj = j % 4
            nr, nc = r + DR[jj], c + DC[jj]
            if 0 <= nr < N and 0 <= nc < N and not medusa_area[sight_dir][nr][nc]:
                d = abs(nr - medusa_pos[0]) + abs(nc - medusa_pos[1])
                if origin_dist < d:
                    continue
                heapq.heappush(cand_pq, (d, j, nr, nc))

        if not cand_pq:
            warrior_map[r][c] += 1
            warriors.append([r, c])
            continue

        _, _, nr, nc = heapq.heappop(cand_pq)
        moved_sum += 1
        warriors.append([nr, nc])
        warrior_map[nr][nc] += 1

    return moved_sum


# -----------------------------
# 4단계: 전사 공격 + 석화 복구
#   - 메두사와 같은 칸 전사 → 공격 성공, 소멸
#   - next_warrior_map에 있던 석화 전사 복구
# -----------------------------
def warriors_attack_and_restore():
    result = 0
    size = len(warriors)
    for _ in range(size):
        r, c = warriors.popleft()
        if r == medusa_pos[0] and c == medusa_pos[1]:
            result += 1
            warrior_map[r][c] -= 1  # 소멸
        else:
            warriors.append([r, c])

    for i in range(N):
        for j in range(N):
            cnt = next_warrior_map[i][j]
            if cnt > 0:
                for _ in range(cnt):
                    warriors.append([i, j])
                warrior_map[i][j] += cnt
                next_warrior_map[i][j] = 0

    return result


# -----------------------------
# 메인 루프
# -----------------------------
def solve():
    out_lines = []
    visited = [[False] * N for _ in range(N)]

    while medusa_pos[0] != park_pos[0] or medusa_pos[1] != park_pos[1]:
        visited[medusa_pos[0]][medusa_pos[1]] = True

        # 1) 메두사 이동 (종료 조건 포함)
        if not move_medusa(out_lines, visited):
            print("".join(out_lines), end="")
            return

        # 2) 메두사 시선(석화)
        kill_count, sight_dir = choose_sight_and_petrify()

        # 3) 전사 이동 (1차 + 2차)
        moved = move_warriors_phase1(sight_dir)
        moved += move_warriors_phase2(sight_dir)

        # 4) 전사 공격
        attack_count = warriors_attack_and_restore()

        out_lines.append(f"{moved} {kill_count} {attack_count}\n")

    # 공원 도착은 move_medusa에서 처리되므로 여기선 턴 출력만 남음
    print("".join(out_lines), end="")


solve()
