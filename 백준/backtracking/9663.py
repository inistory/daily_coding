import sys
input = sys.stdin.readline

N = int(input())
count = 0

cols = [False] * N
diag1 = [False] * (2 * N)
diag2 = [False] * (2 * N)

def dfs(r):
    global count
    if r == N:
        count += 1
        return
    for c in range(N):
        if cols[c] or diag1[r + c] or diag2[r - c + N]: #같은 열, 대각선에 있으면 건너뜀
            continue
        cols[c] = diag1[r + c] = diag2[r - c + N] = True #퀸 놓기
        dfs(r + 1) #다음 행으로 이동
        cols[c] = diag1[r + c] = diag2[r - c + N] = False #퀸 되돌림

dfs(0)
print(count)
