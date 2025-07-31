N = int(input())
answer = set()
for _ in range(N):
    user, state = map(str, input().split())
    if state == 'enter':
        answer.add(user)
    else:
        answer.remove(user)
        
for a in sorted(answer, reverse=True):
    print(a)