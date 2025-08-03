from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
queue = deque()
result = []

for _ in range(N):
    cmd = input().strip().split()
    
    if cmd[0] == 'push':
        queue.append(cmd[1])
    elif cmd[0] == 'pop':
        result.append(queue.popleft() if queue else "-1")
    elif cmd[0] == 'size':
        result.append(str(len(queue)))
    elif cmd[0] == 'empty':
        result.append("0" if queue else "1")
    elif cmd[0] == 'front':
        result.append(queue[0] if queue else "-1")
    elif cmd[0] == 'back':
        result.append(queue[-1] if queue else "-1")

sys.stdout.write('\n'.join(result) + '\n')