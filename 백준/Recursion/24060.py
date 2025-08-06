import sys
sys.setrecursionlimit(10**6)

N, K = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
result = -1

def merge_sort(p, r):#오름차순 정렬
    global cnt, result
    if p < r:
        q = (p + r) // 2 #q는 p,r의 중간지점
        merge_sort(p, q) #전반부정렬
        merge_sort(q + 1, r) #후반부정렬
        merge(p, q, r) #병합

def merge(p, q, r):
    global cnt, result
    tmp = []
    i, j = p, q + 1
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1
    while i <= q:
        tmp.append(A[i])
        i += 1
    while j <= r:
        tmp.append(A[j])
        j += 1
    for i in range(len(tmp)):
        A[p + i] = tmp[i] #tmp에 복사해둔 정렬값 저장
        cnt += 1 #저장할 때마다 cnt+1
        if cnt == K:#k번째저장값을 체크
            result = tmp[i]

merge_sort(0, N - 1)
print(result)
