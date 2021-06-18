def solve(t,p):    
    dp = [0]*15

    for i in range(n):
        if dp[i] > dp[i+1]: # 현재 페이가 다음날 페이보다 높다면
            dp[i+1] = dp[i] # 다음날 페이는 현재로
        if dp[i+t[i]] < dp[i] + p[i]: # T일 후에 받게될 페이가 현재의 페이보다 높다면
            dp[i+t[i]] = dp[i] + p[i] # T일후에 을 넣는다.
        
    print(dp[n])


if __name__ == "__main__":
    n = int(input())
    t, p = [0]*n, [0]*n

    for i in range(n):
        t[i], p[i] = map(int, input().split())

    solve(t,p)
