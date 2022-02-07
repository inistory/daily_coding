#이진탐색 안쓴 것
import sys
input = sys.stdin.readline

n, m =map(int, input().split())
ddok = list(map(int, input().split()))

H = max(ddok)
for h in range(H,min(ddok)-1, -1):
    answer = 0
    for i in range(len(ddok)):
        if h <=ddok[i]:
            answer += ddok[i] - h
    
    if answer >= m:
        print(h)
        break
    