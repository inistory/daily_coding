import sys
N = int(sys.stdin.readline()) 
score = [list(sys.stdin.readline().split()) for _ in range(N)]

score.sort(key=lambda x: ((int(x[3]),int(x[2]),int(x[1])))) 

print(score[-1][0])
print(score[0][0])