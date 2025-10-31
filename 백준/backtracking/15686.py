from itertools import combinations
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

ch = []
h = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            ch.append((i,j))
        if arr[i][j] == 1:
            h.append((i,j))

answer = 10**9
for c in combinations(ch,m):#m개의 치킨집 선택하는 조합
    cgr = []
    for ha, hb in h: #각집마다
        tmp = 10**9
        for ca, cb in c: #가장 가까운 치킨거리를 찾고
            tmp = min(abs(ha-ca) + abs(hb-cb), tmp)
        cgr.append(tmp) #모든 집의 치킨거리를 구하고
    answer = min(answer,sum(cgr)) #치킨집 조합별 치킨거리합 중 최소값을 구함
print(answer)
