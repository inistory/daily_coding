from itertools import permutations

N, M = map(int, input().split())

for i in permutations(range(1, N+1), M):
    if list(i) == sorted(i):
        print(*i)