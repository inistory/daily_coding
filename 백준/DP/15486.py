#퇴사2

N = int(input())
dp = [0]*(N+1)

for i in range(1, N+1):
    t, p = map(int, input().split())
    dp[i] = max(dp[i], dp[i-1])  # 상담을 하지 않는 경우의 최대 수익 갱신
    if i + t <= N+1:  # 상담을 완료할 수 있는 경우
        dp[i+t] = max(dp[i+t], dp[i] + p)  # 상담을 완료하는 날의 최대 수익 갱신

print(max(dp))

    
    