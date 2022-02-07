# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline

n = int(input())

#나누기2,3,5, 뻬기-1 한 값 중에서 최소값을 구하고 1을 더함

d = [0]*30001

for i in range(2, n+1):
    d[i] = d[i-1] +1 #현재 수에서 1을 뺀 값에서의 최적값에서 1을 더한 값
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    if i % 3 == 0:
        d[i] = min(d[i],d[i//3]+1)
    if i % 5 == 0:
        d[i] = min(d[i],d[i//5]+1)

print(d[n])