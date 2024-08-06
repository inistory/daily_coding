#부분수열의 합
from itertools import combinations
N,S = map(int, input().split())

sun = list(map(int,input().split()))
count = 0
for i in range(1,N+1):
    hubo = list(combinations(sun,i))
    for h in hubo:
        if sum(h) ==S:
            count+=1
    
print(count)


