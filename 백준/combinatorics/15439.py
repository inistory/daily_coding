from itertools import permutations

N = int(input())
print(len(list(permutations(range(N),2))))