import sys
input = sys.stdin.readline

# 방향: 문제 기준 (1:상, 2:하, 3:좌, 4:우)
BDR = [-1, 1, 0, 0]
BDC = [0, 0, -1, 1]

# 달팽이 순회 방향: 좌, 하, 우, 상
SR = [0, 1, 0, -1]
SC = [-1, 0, 1, 0]

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
spells = [tuple(map(int, input().split())) for _ in range(M)]

center = (N // 2, N // 2)

# 1) 달팽이 경로 미리 생성 (center 바로 왼쪽부터 시작하여 좌-하-우-상…)
path = []
r, c = center
step = 1
dir_idx = 0
while len(path) < N * N - 1:
    for _ in range(2):  # 같은 step 길이를 두 번 진행
        for _ in range(step):
            r += SR[dir_idx]
            c += SC[dir_idx]
            if 0 <= r < N and 0 <= c < N:
                path.append((r, c))
            if len(path) == N * N - 1:
                break
        dir_idx = (dir_idx + 1) % 4
        if len(path) == N * N - 1:
            break
    step += 1

path_len = len(path)  # N*N - 1

def blizzard(d, s):
    cr, cc = center
    dr, dc = BDR[d - 1], BDC[d - 1]
    for k in range(1, s + 1):
        rr, cc2 = cr + dr * k, cc + dc * k
        if 0 <= rr < N and 0 <= cc2 < N:
            A[rr][cc2] = 0

def board_to_linear():
    # 2) 당기기 전에 보드를 1D로 읽고 0 제거해서 앞으로 당김
    linear = []
    for (r, c) in path:
        if A[r][c] != 0:
            linear.append(A[r][c])
    # 길이 맞춰 0 패딩
    if len(linear) < path_len:
        linear += [0] * (path_len - len(linear))
    else:
        linear = linear[:path_len]
    return linear

def linear_pull(linear):
    # 0 제거 후 앞으로 당김 + 패딩
    nl = [x for x in linear if x != 0]
    if len(nl) < path_len:
        nl += [0] * (path_len - len(nl))
    else:
        nl = nl[:path_len]
    return nl

def explode(linear, score):
    # 3) 연쇄 폭발: 같은 숫자 4개 이상 반복 제거
    exploded_any = False
    i = 0
    while i < path_len and linear[i] != 0:
        j = i
        val = linear[i]
        while j < path_len and linear[j] == val:
            j += 1
        if val != 0 and j - i >= 4:
            # 점수 집계 (문제 조건상 구슬 값은 1,2,3)
            if 1 <= val <= 3:
                score[val] += (j - i)
            for k in range(i, j):
                linear[k] = 0
            exploded_any = True
        i = j
    return exploded_any

def transform(linear):
    # 4) 그룹 변환: (묶음크기, 숫자) 순서로 재배열
    newL = []
    i = 0
    while i < path_len and linear[i] != 0:
        j = i
        val = linear[i]
        while j < path_len and linear[j] == val:
            j += 1
        cnt = j - i
        newL.extend([cnt, val])
        i = j
        if len(newL) >= path_len:
            break
    if len(newL) < path_len:
        newL += [0] * (path_len - len(newL))
    else:
        newL = newL[:path_len]
    return newL

def linear_to_board(linear):
    # 선형 리스트를 보드에 다시 기록
    for idx, (r, c) in enumerate(path):
        A[r][c] = linear[idx]

score = [0, 0, 0, 0]  # score[1], score[2], score[3]

for d, s in spells:
    # 블리자드
    blizzard(d, s)

    # 당기기
    L = board_to_linear()
    L = linear_pull(L)

    # 연쇄 폭발
    while True:
        changed = explode(L, score)
        if not changed:
            break
        L = linear_pull(L)

    # 그룹 변환
    L = transform(L)

    # 보드로 반영
    linear_to_board(L)

# 최종 점수 출력
print(score[1] * 1 + score[2] * 2 + score[3] * 3)
