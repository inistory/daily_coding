from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline
def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array,right_value)#현재 값의 인덱스+1
    left_index = bisect_left(array, right_value)#현재 값의 인덱스
    return right_index - left_index #6 -2


n, x = map(int,input().split()) #7,2
array = list(map(int, input().split()))#1 1 2 2 2 2 3

count = count_by_range(array, x,x)  

if count ==0: 
    print(-1)
else:
    print(count)