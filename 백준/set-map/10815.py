N = int(input())
card = set(map(int, input().split()))

M = int(input())
sang = list(map(int, input().split()))

answer = []
for m in sang:
    if m in card:
        answer.append(1)
    else:
        answer.append(0)

print(*answer)
