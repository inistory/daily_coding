# 입력: 보드의 크기 N (행), M (열)
N, M = map(int, input().split())

# 입력: 보드의 각 줄을 문자열로 받아 리스트로 저장
board = [input() for _ in range(N)]

# 함수: (x, y) 위치를 좌상단으로 하는 8x8 체스판을 만들 때,
# start_color로 시작하는 정상 체스판으로 바꾸기 위해 다시 칠해야 하는 칸 수를 계산
def count_repaint(x, y, start_color):
    repaint = 0
    for i in range(8):  # 8행 반복
        for j in range(8):  # 8열 반복
            # (i + j)가 짝수면 시작색, 홀수면 반대색이 와야 함
            expected = start_color if (i + j) % 2 == 0 else ('B' if start_color == 'W' else 'W')
            # 현재 칸이 기대한 색이 아니라면 칠해야 함
            if board[x + i][y + j] != expected:
                repaint += 1
    return repaint

# 가능한 최소 칠하기 횟수를 저장할 변수 (초기값은 무한대)
min_repaint = float('inf')

# 보드 전체에서 8x8 크기의 서브보드를 탐색 (좌상단 기준)
for i in range(N - 7):  # 최대 N-8+1개의 행에서 시작 가능
    for j in range(M - 7):  # 최대 M-8+1개의 열에서 시작 가능
        # 두 가지 경우 중 더 작은 값을 갱신
        min_repaint = min(
            min_repaint,
            count_repaint(i, j, 'W'),  # 흰색으로 시작하는 체스판
            count_repaint(i, j, 'B')   # 검은색으로 시작하는 체스판
        )

# 결과 출력: 가장 적게 칠한 횟수
print(min_repaint)
