import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]  # 0:빈칸, 1:벽
visited = [[0]*m for _ in range(n)]  # 0:미청소, 1:청소완료

# 0:북, 1:동, 2:남, 3:서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

cleaned = 0

while True:
    # 1) 현재 칸 청소
    if visited[r][c] == 0:
        visited[r][c] = 1
        cleaned += 1

    # 2) 왼쪽부터 4방향 탐색
    moved = False
    for _ in range(4):
        d = (d + 3) % 4  # 왼쪽 회전(서->남->동)
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] == 0 and visited[nr][nc] == 0:
            # 왼쪽에 청소되지 않은 빈 칸 → 그 칸으로 전진
            r, c = nr, nc
            moved = True
            break

    if moved:
        continue  # 전진했으면 다시 1)로

    # 3) 네 방향 모두 불가 → 뒤로 한 칸
    bd = (d + 2) % 4
    br, bc = r + dr[bd], c + dc[bd]
    # 뒤가 벽이면 작동 종료
    if not (0 <= br < n and 0 <= bc < m) or arr[br][bc] == 1:
        break
    # 뒤로만 이동(방향 유지)
    r, c = br, bc

print(cleaned)
