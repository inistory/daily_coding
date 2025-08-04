from collections import deque

N, K = map(int, input().split())
queue = deque(range(1,N+1))
result = []

while queue:
    queue.rotate(-(K - 1))     # K-1만큼 왼쪽으로 회전
    result.append(queue.popleft())  # K번째 사람 제거

print("<" + ", ".join(map(str, result)) + ">")