#1로 만들기
import sys

input = sys.stdin.readline
n = int(input())

dp = [0] * (n + 1)
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1  # 1을 빼는 연산
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)  # 3으로 나누는 연산
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)  # 2로 나누는 연산

print(dp[n])