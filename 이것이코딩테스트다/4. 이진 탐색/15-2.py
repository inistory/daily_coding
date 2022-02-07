# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right
n = int(input())
array = map(int, input().split())

def search(array,start, end):
    while start <= end:
        mid = (start + end)//2

        if array[mid] == mid:
            return mid
        elif array[mid] > mid:
            return search(array, start, mid-1)
        else:
            return search(array, mid+1, end)
            




index = search(array,0, n-1)

if index ==None:
    print(-1)
else:
    print(index)