N = int(input())
arr = []
for _ in range(N):
    arr.append(tuple(map(int, input().split())))
arr.sort()
for a,b in arr:
    print(a,b)