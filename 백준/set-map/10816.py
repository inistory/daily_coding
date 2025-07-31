N = int(input())
sang = list(map(int, input().split()))
M = int(input())
target = list(map(int, input().split()))

from collections import Counter
counter = Counter(sang)
answer = []
for t in list(target):
    answer.append(counter[t])
    
print(*answer)
