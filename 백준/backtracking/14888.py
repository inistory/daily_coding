import sys
sys.setrecursionlimit(10**6)#충분히크게 잡은 값
input = sys.stdin.readline

n = int(input().strip())
nums = list(map(int, input().split()))
plus, minus, mul, divi = map(int, input().split())

MAX, MIN = -10**18, 10**18 #임의로 잡은 아주 작은 값과 아주 큰 값

def div_toward_zero(a, b):
    # 문제 규칙: C++14처럼 0을 향해 버림
    if a * b < 0:
        return -(abs(a) // abs(b))
    return abs(a) // abs(b)

def dfs(idx, val, p, m, u, d):
    global MAX, MIN
    if idx == n:
        if val > MAX: MAX = val
        if val < MIN: MIN = val
        return
    x = nums[idx]
    if p: dfs(idx + 1, val + x, p - 1, m, u, d)
    if m: dfs(idx + 1, val - x, p, m - 1, u, d)
    if u: dfs(idx + 1, val * x, p, m, u - 1, d)
    if d: dfs(idx + 1, div_toward_zero(val, x), p, m, u, d - 1)

dfs(1, nums[0], plus, minus, mul, divi)
print(MAX)
print(MIN)