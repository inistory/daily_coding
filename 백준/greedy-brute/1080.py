import sys
input = sys.stdin.readline

# 입력 받기
N, M = map(int, input().split())
A = [list(map(int, input().strip())) for _ in range(N)]
B = [list(map(int, input().strip())) for _ in range(N)]

# 3x3 뒤집기 함수
#좌상단이 (x, y)인 3×3 부분을 0↔1 반전
def flip(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            A[i][j] = 1 - A[i][j]
#(0, 0)부터 (N-3, M-3)까지 반복
# A[i][j] != B[i][j]인 지점을 기준으로 flip(i, j)
# 가능한 가장 앞에서 바꾸는 것이 최소 횟수
count = 0
for i in range(N - 2):#이 위치에 있어야 3x3flip이 가능해서
    for j in range(M - 2):
        if A[i][j] != B[i][j]:  # 다르면 flip 수행
            flip(i, j)
            count += 1

# 결과 확인
if A == B:
    print(count)
else:
    print(-1)