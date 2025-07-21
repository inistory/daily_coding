N = int(input())
current = 0
count=0 #666수 세기
while True:
    current+=1
    if "666" in str(current):
        count+=1
        if count == N:
            print(current)
            break