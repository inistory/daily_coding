import math
T = int(input())

def is_prime(x):
    if x%2 == 0:
        return False
    limit = int(math.isqrt(x))
    for i in range(3,limit+1,2):
        if x%i == 0:
            return False
    return True

for _ in range(T):
    n = int(input())
    if n <= 2: #N이 2와 같거나 작다면
        print(2)
        continue
    while True:
        if is_prime(n):
            print(n)
            break
        n+=1