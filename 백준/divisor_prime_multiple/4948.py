import math
def is_prime(x):
    if x==2:
        return True
    if x<2 or x%2==0:
        return False
    limit = math.isqrt(x)
    for i in range(3, limit+1, 2):
        if x%i == 0:
            return False

    return True
while True:
    n = int(input())
    if n==0:
        break
    count = 0
    for i in range(n+1,2*n+1):
        if is_prime(i):
            count+=1
    print(count)