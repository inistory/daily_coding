import sys
sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = list(range(n + 1))
size = [1] * (n + 1)

def find(x):
    # 경로 압축
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return
    # 작은 트리를 큰 트리에 붙인다 (union by size)
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]

out = []
for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0:
        union(a, b)
    else:  # op == 1
        out.append("YES" if find(a) == find(b) else "NO")

print("\n".join(out))
