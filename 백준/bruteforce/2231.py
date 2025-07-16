N = int(input())
result = 0

#M의 최소값이 N-9*len(str(N))
for i in range(max(1, N - 9 * len(str(N))), N):
    if i + sum(map(int, str(i))) == N:
        result = i
        break

print(result)