N = int(input())
db = list(map(int,input().split()))
db.sort()

answer = 0
for i in range(N):
    answer+=sum(db[:i+1])
    
print(answer)