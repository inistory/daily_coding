#-*- coding: utf-8 -*-
import sys
input = sys.stdin.readline

n = int(input())
ary = list(map(int, input().split()))
ary.sort()
left = 0 #맨 앞
right = n-1 #맨 끝

min_hab = 2000000001
answer = []

while left < right:
    L = ary[left]
    R = ary[right]

    hab = L + R 
    # 두 용액의 합이 0과 가장 가까운 용액을 정답에 담아주기
    if abs(hab) < min_hab: 
        min_hab = abs(hab)
        answer = [L, R]
        
    # 두 용액의합이 0보다 작다면 왼쪽의 값을 늘려 0에 가깝게
    if hab < 0:
        left += 1
    # 반대로, 두 용액의 합이 0보다 크다면 오른쪽의 값을 줄여서 0에 가깝게
    else:
        right -= 1

print(answer[0], answer[1])