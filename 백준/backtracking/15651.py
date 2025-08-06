from itertools import product

N, M = map(int, input().split())

for i in product(range(1,N+1),repeat=M):
    print(*i)