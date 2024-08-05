from collections import deque

arr = [list(map(int, input().split())) for _ in range(5)]

def bfs(x,y, string):
    queue = deque()
    queue.append((x,y,string))
    nx = [0,0,-1,1]
    ny = [-1,1,0,0]
    
    while queue:
        x,y,string = queue.popleft()
        string += str(arr[x][y])
        
        if len(string)==6:
            answer.append(string)
            continue #다음루프로 넘어가겠다->다음while문을 돈다.
        
        for k in range(4):
            dx = x + nx[k]
            dy = y + ny[k]
            if 0<=dx<5 and 0<=dy<5:
                queue.append((dx,dy,string))

answer = []   
for x in range(5):
    for y in range(5):
        bfs(x,y,'')

print(len(set(answer)))