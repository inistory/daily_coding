n = int(input())
num = list()
for i in range(n):
    num.append(int(input()))
    
num.sort()
for i in range(n):
    print(num[i])
