N,M = map(int,input().split())
N_arr = set()
M_arr = set()
for _ in range(N):
    N_arr.add(input().strip())

for _ in range(M):
    M_arr.add(input().strip())
NM_arr = (N_arr & M_arr)

print(len(NM_arr))
for NM in sorted(NM_arr):
    print(NM)