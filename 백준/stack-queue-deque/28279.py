from collections import deque
import sys
input = sys.stdin.readline
dq = deque()

N = int(input())

for _ in range(N):
    cmd = input().split()
    op = cmd[0]
    if op == '1':
        dq.appendleft(cmd[1])
    elif op == '2':
        dq.append(cmd[1])
    elif op == '3':
        print(dq.popleft() if dq else -1)
    elif op == '4':
        print(dq.pop() if dq else -1)
    elif op == '5':
        print(len(dq))
    elif op == '6':
        print(0 if dq else 1)
    elif op == '7':
        print(dq[0] if dq else -1)
    elif op == '8':
        print(dq[-1] if dq else -1)