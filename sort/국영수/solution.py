import sys 
N = int(sys.stdin.readline()) 
score = [list(sys.stdin.readline().split()) for _ in range(N)]

score.sort(key=lambda x: (-int(x[1]),int(x[2]),-int(x[3]),x[0])) #국어성적이 감소하는 순서

for t in score:
    print(t[0])
