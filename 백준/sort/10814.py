N = int(input())
arr = []
for _ in range(N):
    age, name = input().split()
    arr.append((int(age), name))
    
arr.sort(key=lambda a:(a[0]))

for age, name in arr:
    print(age, name)