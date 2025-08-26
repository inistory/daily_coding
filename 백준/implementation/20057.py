import sys
input = sys.stdin.readline

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

# 이동 순서: 왼(0) → 아래(1) → 오른(2) → 위(3)
DR = [0, 1, 0, -1]
DC = [-1, 0, 1, 0]

#spread[0]: 왼쪽으로 이동할 때 모래 분배 패턴 정의(dr, dc, percent) -> 하드코딩
#spread[1]~spread[3]: 아래, 오른쪽, 위로 이동할 때 퍼짐 -> 자동생성
#즉, spread를 보면 모래를 어디로 퍼뜨려야 할지를 바로 알 수 있음
BASE = [
    (-1,  1,  1),#1%
    ( 1,  1,  1),
    (-2,  0,  2),#2%
    ( 2,  0,  2),
    ( 0, -2,  5),#5%
    (-1,  0,  7),#7%
    ( 1,  0,  7),
    (-1, -1, 10),#10%
    ( 1, -1, 10),
]
ALPHA_BASE = (0, -1)  # 남은 모래(α) 위치: 남은 모래 가는 곳

#방향별 분배 좌표 생성
def rotate_cw(dr, dc):
    # 죄표기준 시계 방향 90도 회전: (dr, dc) -> (-dc, dr)
    return (-dc, dr)

# 네 방향(왼/아래/오른/위)으로 패턴 생성
spread = [[] for _ in range(4)]
alpha = [None] * 4

spread[0] = BASE[:]# 왼쪽(하드코딩)
alpha[0] = ALPHA_BASE

for d in range(1, 4):# 아래(1), 오른(2), 위(3)
    cur = []
    for r, c, p in spread[d - 1]:#이전방향 퍼짐패턴
        nr, nc = rotate_cw(r, c)#꺼낸 (r,c)를 90도로 회전(nr,nc)는 새로운 방향의 퍼짐 위치
        cur.append((nr, nc, p))#(nr,nc)와 원래 비율 p를 묶어서 현재 방향(d)의 퍼짐 패턴 리스트인 cur에 추가
    spread[d] = cur#방금 회전해서 만든 cur리스트를 spread[d]에 저장
    ar, ac = rotate_cw(*alpha[d - 1])#알파는 따로 저장 alpha[d - 1]는 이전 방향의 알파 좌표,rotate_cw시계 방향으로 회전
    alpha[d] = (ar, ac)#이번 방향의 알파좌표로 저장 

def inside(r, c):
    return 0 <= r < N and 0 <= c < N

# 시뮬레이션
# This part of the code initializes the variables for the simulation of a sandstorm (토네이도). Here is what each variable represents:
r = c = N // 2 #토네이도 시작 위치 (정중앙)
out_sand = 0 #격자 밖으로 나간 모래 누적값
step = 1 #토네이도가 한 방향으로 이동할 칸 수(두번반복후 하나 증가)
d = 0 #현재 방향 (0: 왼쪽부터 시작)

while True:
    for _ in range(2):  # 같은 step을 두 번 반복
        for _ in range(step): #현재방향으로 step만큼 이동
            r += DR[d]
            c += DC[d]

            y = A[r][c] #현재 칸의 모래양 확인
            if y:#이동한 칸에 모래가 있다면
                used = 0#지금까지 퍼뜨린 총 모래
                for dr, dc, p in spread[d]: #spread[d]방향 기준으로 퍼뜨림
                    amt = (y * p) // 100 #y의 p%만큼의 모래양(실제로 퍼지는 모래 양)
                    nr, nc = r + dr, c + dc #퍼질방향
                    if inside(nr, nc): #격자 안에 있으면
                        A[nr][nc] += amt #그 칸에 모래를 더해주고
                    else: #격자 밖이면
                        out_sand += amt #outsand에 더함
                    used += amt #지금까지 퍼뜨린 총 모래

                # α 위치
                ar, ac = r + alpha[d][0], c + alpha[d][1]
                remain = y - used #남은모래 = 전체모래 - 지금까지 퍼뜨린 총 모래
                if inside(ar, ac): #격자 안에 있으면
                    A[ar][ac] += remain #그 칸에 모래를 더해주고
                else:#격자 밖이면
                    out_sand += remain #out_sand에 더함

                A[r][c] = 0 #원래 칸은 모래 0으로 비움(모래는 전부 퍼졌으므로 비워야 함)
# The code snippet `if r == 0 and c == 0: #좌쵸(0,0) print(out_sand) sys.exit(0)` is checking if the current position of the sandstorm (r, c) is at the coordinates (0, 0) which represents the top-left corner of the grid.

            if r == 0 and c == 0:#문제에서의 (1,1) = 좌표에서는 (0,0)에 도달하면 종료
                print(out_sand) #격자 밖으로 나간 모래량 출력
                sys.exit(0) #종료

        d = (d + 1) % 4 #방향 전환(0->1->2->3->0)
    step += 1 #step+1
