# Track A: 회전 + 그룹핑(예술성 계열) 스켈레톤
# 입력 포맷: N  ->  다음 줄부터 N줄의 정수 격자 (공백 구분)
# 예시 실행: python trackA.py < inputs/A1.txt
from collections import deque

DIR4 = [(-1,0),(0,1),(1,0),(0,-1)]#상,우,하,좌

#outofbound
def oob(i, j, n):
    return i < 0 or j < 0 or i >= n or j >= n


# [1] 같은 값 그룹 라벨링
def group_label(board):
    n = len(board)
    gid = [[-1]*n for _ in range(n)]
    groups = []  # groups[g] = (value, size)
    g = 0
    for i in range(n):
        for j in range(n):
            if gid[i][j] != -1:
                continue
            val = board[i][j]#현재값
            q = deque([(i, j)])
            gid[i][j] = g #좌표별로 그룹아이디정리
            size = 1 #사이즈 초기화
            while q:
                x, y = q.popleft()
                for di, dj in DIR4:
                    nx, ny = x + di, y + dj
                    if oob(nx, ny, n) or gid[nx][ny] != -1:
                        continue
                    if board[nx][ny] != val:#같은그룹을 찾는거니까
                        continue
                    #격자 안에 있고, 방문한적이 없으며, 현재값과 같으면
                    gid[nx][ny] = g #nx,ny의 gid를 기록
                    size += 1 #사이즈 늘림
                    q.append((nx, ny)) #큐에 추가
            groups.append((val, size)) #그룹의 값과 size를 기록
            g += 1
    return gid, groups

# [2] 그룹 간 접촉면 기반 점수 (문제 식에 맞게 바꿔 사용)
def score(board, gid, groups):
    n = len(board)
    total = 0
    for i in range(n):
        for j in range(n):
            g1 = gid[i][j]# (i,j)의 그룹ID
            v1, s1 = groups[g1]# 그 그룹의 (값, 크기)

            # 오른쪽 이웃과의 '경계'를 한 번만 체크
            if j + 1 < n:
                g2 = gid[i][j+1]
                if g1 != g2:# 서로 다른 그룹이면
                    v2, s2 = groups[g2]
                    # 문제 공식에 맞게 바꿔 쓰기
                    total += (s1 + s2) * (v1 * v2)

            # 아래 이웃과의 '경계'를 한 번만 체크
            if i + 1 < n:
                g2 = gid[i+1][j]
                if g1 != g2:
                    v2, s2 = groups[g2]
                    total += (s1 + s2) * (v1 * v2)
    return total


# [3] 회전 (십자 + 4사분면 90도 회전) — 예시 규칙
#홀수N전용
def rotate(board):
    n = len(board)
    mid = n // 2
    old = [row[:] for row in board]#원본

    # (a) 중앙 십자 회전: 가운데 행/열 교환(예시)
    for i in range(n):
        board[i][mid] = old[mid][i]          # 세로 열 <- 가로 행
        board[mid][n-1-i] = old[i][mid]      # 가로 행 <- 세로 열(반전)
    # (b) 4사분면 90도 시계 회전
    # x0,y0 부분 정사각형(사분면)의 왼위 좌표
    # sz 한변의길이
    def rot90_sub(x0, y0, sz):
        for i in range(sz):
            for j in range(sz):
                board[x0 + j][y0 + sz - 1 - i] = old[x0 + i][y0 + j]

    sz = n // 2 #한 변의 길이
    rot90_sub(0, 0, sz)               # 좌상
    rot90_sub(0, mid + 1, sz)         # 우상
    rot90_sub(mid + 1, 0, sz)         # 좌하
    rot90_sub(mid + 1, mid + 1, sz)   # 우하

#짝수N전용
def rotate_quadrants_even(board):
    n = len(board)
    mid = n // 2
    old = [row[:] for row in board]

    def rot90_sub(x0, y0, sz):  # 시계 90°
        for i in range(sz):
            for j in range(sz):
                board[x0 + j][y0 + sz - 1 - i] = old[x0 + i][y0 + j]

    sz = mid  # 한 변 길이 = n//2
    rot90_sub(0, 0,sz)  # 좌상
    rot90_sub(0,mid,sz)  # 우상   ← 짝수는 여기서 mid (mid+1 아님)
    rot90_sub(mid,0,sz)  # 좌하
    rot90_sub(mid,mid,sz)  # 우하


###main
n = int(input().strip())
board = [list(map(int, input().split())) for _ in range(n)]
# print('board:')
# for b in board:
#     print(b)
# TODO: 문제에 따라 라운드 수를 입력으로 받는다면 아래로 교체
# R = int(input().strip())
R = 1
total = 0
for _ in range(R):
    gid, groups = group_label(board)
    total += score(board, gid, groups)
    # print(total)
    rotate(board)
    print(board)
# print(total)


