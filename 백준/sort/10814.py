N = int(input())
arr = []
for _ in range(N):
    arr.append(str(input()))
    
arr.sort(key=lambda a: (len(a),a))

for a in arr:
    print(a)
