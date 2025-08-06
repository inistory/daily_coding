import sys
input = sys.stdin.readline

def cantor(n):
    if n == 0:
        return "-"
    part = cantor(n - 1)
    return part + " " * (3**(n-1)) + part

while True:
    try:
        N = int(input().strip())
    except:
        break
    print(cantor(N))
