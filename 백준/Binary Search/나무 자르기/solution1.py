import sys
input = sys.stdin.readline

n, m =map(int, input().split())
tree = list(map(int, input().split()))

start = 0
end = max(tree)
result = 0
while start <= end:
    mid = (start + end) //2
    #h기준으로 자른 후 가져갈 수 있는 나무 길이 total
    total = 0
    for i in range(n):
        if tree[i] > mid:
            total += tree[i] - mid

    if total < m : #나무길이가 부족하면 mid를 앞쪽으로
        end = mid-1

    else: #나무양이 충분하면 저장
        start = mid+1
        result = mid

print(result)
