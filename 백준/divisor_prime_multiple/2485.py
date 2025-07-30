from math import gcd

n = int(input())
trees = [int(input()) for _ in range(n)]

# 각 나무 사이 거리 계산
distances = [trees[i+1] - trees[i] for i in range(n - 1)]
print(distances)
# 모든 거리의 최대공약수(GCD) 구하기
g = distances[0]
for d in distances[1:]:
    g = gcd(g, d)

# 각 간격마다 새로 심어야 할 나무 수 계산
result = sum((d // g - 1) for d in distances)

# 출력
print(result)
