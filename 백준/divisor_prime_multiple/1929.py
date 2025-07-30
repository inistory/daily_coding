import math
M,N = map(int, input().split())

def is_prime(x):
    if x == 2:
        return True
    if x < 2 or x%2==0:
        return False
    limit = int(math.isqrt(x))
    for i in range(3,limit+1,2):
        if x%i==0:
            return False
    return True
for n in range(M,N+1):
    if is_prime(n):
        print(n)