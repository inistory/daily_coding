import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
warp = {}
for _ in range(N + M):
    a, b = map(int, input().split())
    warp[a] = b

# dist[i] = i번 칸에 도달하기까지 필요한 최소 주사위 굴림 수
dist = [-1] * 101 #1번 칸에서 i번 칸까지 가는 데 필요한 최소 주사위 횟수: -1로 초기화
q = deque([1])#1칸에서 시작(큐선언 및 1 append를 한 번에:q = deque() + q.append(1))
dist[1] = 0

while q:
    now = q.popleft()
    if now == 100:#최종칸 도달
        print(dist[now])
        break

    for dice in range(1, 7):#현재칸 x에서 주사위 1~6 모두 시도
        nxt = now + dice
        if nxt > 100:#100넘으면 스킵
            continue
        if nxt in warp: #사다리나 뱀이 있으면 자동이동
            nxt = warp[nxt]
        if dist[nxt] == -1:#처음 가보는 칸이면
            dist[nxt] = dist[now] + 1 #현재까지 굴린 횟수+1해서 기록
            q.append(nxt)#다음에도 이 칸에서 주사위 굴려볼 수 있도록 큐에 넣기