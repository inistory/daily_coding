#미친 로봇
import sys
input = sys.stdin.readline

nn, e, w, s, n = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
arr = [e * 0.01, w * 0.01, s * 0.01, n * 0.01]

visited = [[0] * (2 * nn + 1) for _ in range(2 * nn + 1)]
visited[nn][nn] = 1
answer = 0

def dfs(x, y, per, count):
    global answer
    if count == nn:
        answer += per
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if visited[nx][ny]:
            continue
        visited[nx][ny] = 1
        dfs(nx, ny, per * arr[i], count + 1)
        visited[nx][ny] = 0

dfs(nn, nn, 1, 0)

print(answer)