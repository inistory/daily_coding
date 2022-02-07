import sys
input = sys.stdin.readline

n = int(input())

food = map(int, input().split())

d = [0]*100

d[0] = food[0]
d[1] = max(food[0],food[1])

for i in range(2,n):
    d[i] = max(d[i-2]+food[i], d[i-1])


print(d[n-1])