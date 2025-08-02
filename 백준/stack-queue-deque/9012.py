T = int(input())
for _ in range(T):
    stack = []
    arr = input()
    is_vps = True
    for a in arr:
        if a == '(':
            stack.append(a)
        elif a == ')':
            if not stack:
                is_vps = False
                break
            else:
                stack.pop()
    if is_vps and not stack:
        print('YES')
    else:
        print('NO')