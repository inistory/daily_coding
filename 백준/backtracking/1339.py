#단어 수학

N = int(input()) 

arr = []#단어모음
dic = {}
for n in range(N):
    a = input()
    arr.append(a)
    

for i in range(N): #GCF,ACDEB
    for j in range(len(arr[i])): #GCF길이만큼, ACDEB길이만큼
        if str(arr[i][j]) not in dic:
            dic[str(arr[i][j])] = 10 ** (len(arr[i]) -j - 1)
        else:
            dic[str(arr[i][j])] += 10 ** (len(arr[i]) -j - 1)

arr2 = []
for value in dic.values():
    arr2.append(value)

arr2.sort(reverse=True)
answer = 0
for i in range(len(arr2)):
    answer+=arr2[i]*(9-i)
    
print(answer)