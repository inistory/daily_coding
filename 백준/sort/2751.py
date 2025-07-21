import sys #시간초과나서 이걸로해야함

N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]

arr.sort()

for a in arr:
    print(a)
