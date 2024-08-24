from itertools import combinations

while True:
    arr = list(map(int,input().split()))

    k = arr[0]
    
    for i in list(combinations(arr[1:],6)):
        print(*i)
        
    if k == 0:
        exit()
    print()