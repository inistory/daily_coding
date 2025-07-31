import sys
input = sys.stdin.readline

MAX = 1_000_000
is_prime = [True] * (MAX + 1)
is_prime[0] = is_prime[1] = False

# 에라토스테네스의 체로 소수 판정
for i in range(2, int(MAX**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, MAX + 1, i):
            is_prime[j] = False

T = int(input())
for _ in range(T):
    n = int(input())
    count = 0
    # i와 n‑i 모두 소수이면 카운트
    for i in range(2, n // 2 + 1):
        if is_prime[i] and is_prime[n - i]:
            count += 1
    print(count)
