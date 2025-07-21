arr = []
for _ in range(5):
    arr.append(int(input()))

print(int(sum(arr)/len(arr)))
arr.sort()
print(arr[len(arr)//2])