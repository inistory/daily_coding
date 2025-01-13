n = int(input())
a = list(map(int, input().split()))

def check_prime(aa):
    if aa <= 1:
        return False
    for i in range(2, int(aa**0.5) + 1):
        if aa % i == 0:
            return False
    return True

count = 0
for aa in a:
    if check_prime(aa):
        count += 1

print(count)