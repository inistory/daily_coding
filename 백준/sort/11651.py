N = int(input())
arr = []
for _ in range(N):
    arr.append(tuple(map(int,input().split())))

arr.sort(key=lambda p: (p[1],p[0])) #매개변수:반환값
for a, b in arr:
    print(a,b)