#가장 긴 감소하는 부분 수열

n = int(input())

arr = list(map(int, input().split()))
dp = [1] * n

#가장 긴 부분 수열의 길이 저장
for i in range(n):
    for j in range(i): #이전 값들과 비교
        if arr[i] < arr[j]: #감소하는 수열이어야 함
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
