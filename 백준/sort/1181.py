N = int(input())
arr = []
for _ in range(N):
    arr.append(str(input()))

arr = list(set(arr))
arr.sort(key=lambda a: (len(a),a)) #매개변수:반환값
for a in arr:
    print(a)