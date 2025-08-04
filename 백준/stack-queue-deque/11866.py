from collections import deque

N, K = map(int, input().split())
queue = deque(range(1,N+1))
result = []

while queue:
    queue.rotate(-(K - 1))     # K-1만큼 왼쪽으로 회전(K번째 사람이 맨 앞으로 오게 만듦)
    result.append(queue.popleft())  # 멘 앞에 있는 K번째 사람 제거

print("<" + ", ".join(map(str, result)) + ">")