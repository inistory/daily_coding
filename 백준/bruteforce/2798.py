from itertools import combinations

N,M = map(int, input().split())
arr = list(map(int, input().split()))

max_sum  = 0
for com in combinations(arr,3):
    if sum(com)<=M:
        max_sum = max(max_sum,sum(com))

print(max_sum)