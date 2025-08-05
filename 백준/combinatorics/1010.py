import math
T = int(input())

for _ in range(T):
    W,E = map(int, input().split())
    print(math.comb(E,W)) #더 큰 수를 먼저