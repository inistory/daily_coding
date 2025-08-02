while True:
    string = input()
    stack = []
    is_vps = True
    if string == '.':
        break
    for s in string:
        if s in ('(','['):
            stack.append(s)
        if s in (')',']'):
            if not stack:
                is_vps=False
                break
            else:
                if stack[-1]  == '[' and s == ']':
                    is_vps = True
                    stack.pop()
                elif stack[-1]  == '(' and s == ')':
                    is_vps = True
                    stack.pop()
                else:
                    is_vps = False
                    break
                
    if is_vps and not stack:
        print('yes')
    else:
        print('no')