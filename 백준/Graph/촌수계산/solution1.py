def bfs(start, end):

    queue = [start]
    visited = []

    while queue:
        current = queue.pop(0)
        visited.append(current)
        if current==end:
            break
        for c in arr[current]:
            if c not in visited:
                record[c] = record[current] + 1
                queue.append(c)

    if record[end] == 0:
        print(-1)
    else:
        print(record[end])

n = int(input()) #사람 수 = vertex
a, b = map(int ,input().split())  #촌수를 계산해야하는 두 사람의 번호
m = int(input()) #관계의 수 =edge

#관계저장을 위한 list
arr = [[] for _ in range(n+1)]

#방문 기록
record = [0] * (n+1)

#관계저장 = adjacencylist
for _ in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)

bfs(a,b)
