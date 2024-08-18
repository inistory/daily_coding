#퇴사

import sys
input = sys.stdin.readline
def dfs(day, profit):
    global answer
    if day == n + 1:
        answer = max(answer, profit)
        return
    if day + t[day] <= n + 1:
        dfs(t[day] + day, profit + p[day])
    dfs(day + 1, profit)


n = int(input())
t = [0]
p = [0]
answer = 0

for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

for i in range(1, n + 1):
    dfs(i, 0)
print(answer)