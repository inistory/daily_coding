#-*- coding: utf-8 -*-
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

ary = list(map(int,input().split()))

hab = 0
end = 0
result = 0
# start를 차례대로 증가시키며 반복
for start in range(n):
    #end를 가능한 만큼 오른쪽으로 이동시키기
    while hab < m and end < n:
        hab += ary[end]
        end+=1
    if hab == m:
        result+=1
    #부분합이 m과 같거나 클 때, start를 오른쪽으로 이동
    hab -= ary[start]

print(result)