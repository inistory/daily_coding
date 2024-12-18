from itertools import combinations

def solution(number):
    count = 0
    for n in list(combinations(number,3)):
        if sum(n) == 0:
            count+=1
    
    return count