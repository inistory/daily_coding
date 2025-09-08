import sys
from collections import deque
input = sys.stdin.readline

# 방향: 0=UP, 1=DOWN, 2=LEFT, 3=RIGHT
DIRS = [(-1,0),(1,0),(0,-1),(0,1)]
F_MAP = {'T':1, 'C':2, 'M':4}  # 민트/초코/우유 → 비트마스크
#민트(T)->1->001
#초코(C)->2->010
#우유(M)->4->100
#민트+초코->001|010=011->3
#민트+우유->001|100=101->5
#초코+우유->010|100=110->6
#민트+초코+우유->111->7

N, T = map(int, input().split())
#공백과양쪽공백제거
F_chars = [list(input().replace(" ", "").strip()) for _ in range(N)]
F = [[F_MAP[ch] for ch in row] for row in F_chars]
B = [list(map(int, input().split())) for _ in range(N)]


def lunch():
    """같은 F로 연결된 컴포넌트별 대표 선정 및 점심 신앙심 갱신."""
    visited = [[False]*N for _ in range(N)]
    leaders = [[False]*N for _ in range(N)]#각 칸이 대표인지 여부 저장
    #모든 칸 순회하면서
    for sr in range(N):
        for sc in range(N):
            if visited[sr][sc]:
                continue
            #방문하지 않은 칸에서 DFS시작
            food = F[sr][sc]#시작 음식
            q = deque([(sr, sc)])
            visited[sr][sc] = True
            comp = [(sr, sc)]#bfs로 같은 F값을 인접한 칸들 모음
            while q:
                r, c = q.popleft()
                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    #격자 밖이면 무시, 방문했으면 무시
                    if not (0 <= nr < N and 0 <= nc < N) or visited[nr][nc]:
                        continue
                    #인접한 칸의 음식이 현재 그룹음식 f와 다르면 컨포넌트가 아님
                    if F[nr][nc] != food:
                        continue
                    #같은음식이고 아직 방문을 안했으니 BFS에 포함, 방문표시
                    visited[nr][nc] = True
                    q.append((nr, nc))
                    comp.append((nr, nc))
            # 대표자 선정: 신앙심 내림차순, 행 오름차순, 열 오름차순
            lr, lc = min(comp, key=lambda x: (-B[x[0]][x[1]], x[0], x[1]))
            leaders[lr][lc] = True#대표좌표기록
            size = len(comp)#그룹크기(같은 신봉자수를 계산
            if size > 1:#크기가 2이상이라면
                for r, c in comp:
                    if r == lr and c == lc:
                        B[r][c] += (size - 1)#그룹인원수-1
                    else:#그 외 구성원
                        B[r][c] -= 1#신앙심-1
    return leaders#각 칸이 대표인지 여부를 담은 배열

def evening(leaders):
    """대표자 전파. 그룹 순서: 단일 → 이중 → 삼중. 그룹 내 우선순위 정렬."""
    # 대표자들을 F별로 모으기
    buckets = {1:[], 2:[], 4:[], 3:[], 5:[], 6:[], 7:[]}
    for r in range(N):
        for c in range(N):
            if leaders[r][c]:
                buckets[F[r][c]].append((r, c))

    # 그룹 순서: 단일(1,2,4) → 이중(6,5,3) → 삼중(7)
    groups = [
        [1, 2, 4],#단일
        [6, 5, 3],#이중(초코우유,민트우유,민트초코)
        [7]#삼중
    ]

    # 전파 타겟 방어 표시 (저녁 동안만 유효)
    #저녁에 전파를 시도당한 학생은 그날 저녁동안 전파자가 될 수 없다.
    defense = [[False]*N for _ in range(N)]

    for masks in groups:
        cand = []
        for m in masks:
            cand.extend(buckets[m])#음식종류m을 가진 대표자들의 좌표 리스트
        #단일그룹의 대표자 후보: 신앙심큰순, 행작은순, 열작은순
        cand.sort(key=lambda x: (-B[x[0]][x[1]], x[0], x[1]))

        #정렬된 대표 후보 좌표들을 하나씩 순회
        for r, c in cand:
            if defense[r][c]:#그날 저녁에 이미 전파 당한 칸(방어상태)면
                continue  #그 학생은 전파자로 활동불가,건너뜀
            spread_food = F[r][c] #현재전파자가 가지고 있는 음식종류 기록
            dir_idx = B[r][c] % 4 #전파방향(0상,1하,2좌,3우)
            x = B[r][c] - 1 #간절함(전파에너지)=대표의신앙심-1
            B[r][c] = 1#전파 시작과 함께 대표 신앙심은 1로 변경
            sr, sc = r, c

            while x > 0:#간절함(전파에너지)가 남아있는 동안 계속 전파 시도
                #현재 위치 (sr,sc)에서 전파 방향 dir_idx(0상,1하,2좌,3우)로 한 칸 전진
                nr, nc = sr + DIRS[dir_idx][0], sc + DIRS[dir_idx][1]
                #격자 밖이면 종료
                if not (0 <= nr < N and 0 <= nc < N):
                    break
                #전파자가 가진 음식(spread_F)와 같은 음식을 만나면 전파안함
                if F[nr][nc] == spread_food:
                    sr, sc = nr, nc
                    continue #그 칸은 건너뛰고 계속 전진
                #다른 음식을 만나면,
                y = B[nr][nc] #그 학생의 현재 신앙심(y)를 읽고
                defense[nr][nc] = True  #그 학생을 방어상태로 표시

                if x > y:#간절함x가 상대 신앙심 y보다 크다면(강한전파)
                    x -= (y + 1)#전파자의에너지x를 y+1만큼 소모하고
                    if x < 0: x = 0 #x가 될 수 있는 최소값은0
                    B[nr][nc] = y + 1 #대상의 신앙심은+1
                    F[nr][nc] = spread_food #대상의 음식을 전파자의 음식으로 교체
                    sr, sc = nr, nc #그 칸으로 이동해서 전파 계속
                else:# 약한 전파
                    B[nr][nc] = y + x #대상의 신앙심을 y+x로 올리고
                    F[nr][nc] = spread_food | F[nr][nc] #음식 혼합
                    x = 0 #전파자의 에너지는 소진
                    break #전파종료

for _ in range(T):
    # 아침
    for i in range(N):
        for j in range(N):
            B[i][j] += 1

    # 점심
    leaders = lunch()

    # 저녁
    evening(leaders)

    # 각 음식 신봉자들의 신앙심 총합 출력
    # 출력순서: 민초우(7), 민초(3), 민우(5), 초우(6), 우(4), 초(2), 민(1)
    sums = {1:0, 2:0, 4:0, 3:0, 5:0, 6:0, 7:0}
    for i in range(N):
        for j in range(N):#그 칸의 음식종류를 키로 해서
            sums[F[i][j]] += B[i][j]#신앙심을 합산
    order = [7, 3, 5, 6, 4, 2, 1]
    print(' '.join(str(sums[m]) for m in order))
