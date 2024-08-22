#일곱 난쟁이
from itertools import combinations
arr = []
for i in range(9):
    arr.append(int(input()))
    
arr.sort()
for a in list(combinations(arr,7)):
    if sum(a) == 100:
        for aa in a:
            print(aa)
        break