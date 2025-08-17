import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]
coin.sort(reverse=True)

ans = 0
for c in coin:
    if K == 0:
        break
    if c <= K:
        cnt = K // c
        ans += cnt
        K %= c

print(ans)