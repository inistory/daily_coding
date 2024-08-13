#계단 오르기
n = int(input())
stairs = [0] + [int(input()) for _ in range(n)]  # 계단 점수, 1번째 인덱스부터 시작
dp = [0] * (n + 1)  # dp 배열 초기화

# 초기 조건 설정
dp[1] = stairs[1]
if n > 1:
    dp[2] = stairs[1] + stairs[2]

# 점화식 적용
for i in range(3, n + 1):
    dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])

# 결과 출력
print(dp[n])