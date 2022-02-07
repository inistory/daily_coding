# -*- coding: utf-8 -*-
#이진탐색 쓴 것ㄴ
import sys
input = sys.stdin.readline

n, m =map(int, input().split())
ddok = list(map(int, input().split()))
# print(ddok)

start = 0
end = max(ddok)
total = 0
result = 0
while start <= end:
    mid = (start + end) //2
    #h기준으로 자른 후 가져갈 수 있는 떡볶이 길이 total
    total = 0
    for i in range(len(ddok)):
        if ddok[i] > mid:
            total += ddok[i] - mid  

    if total == m:
        result = mid
        break
    if total < m : #떡양이 부족하면 h(mid)를 앞쪽으로
        end = mid-1
        
    else: #떡양이 충분하면 저장
        start = mid+1
        result = mid
    
print(result)

    