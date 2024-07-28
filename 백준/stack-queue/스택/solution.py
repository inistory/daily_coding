import sys
N = int(sys.stdin.readline())

stack = []
for i in range(0,N):
    cal = list(sys.stdin.readline().split())
    if cal[0] == 'push':
        stack.append(cal[1])
    elif cal[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(int(stack.pop()))
    elif cal[0] == 'size':
        print(len(stack))
    elif cal[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) != 0:
            print(int(stack[-1]))
        else:
            print(-1)
        
