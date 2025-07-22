N, M = map(int, input().split())
S = set()
check_str = []
for _ in range(N):
    S.add(input())
    
count = 0
for _ in range(M):
    word = input()
    if word in S:
        count += 1

print(count)