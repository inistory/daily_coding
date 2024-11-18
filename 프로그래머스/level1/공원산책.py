def solution(park, routes):
    m = {'N':(-1,0),'S':(1,0),'W':(0,-1),'E':(0,1)}
    cur = [0,0]
    #시작지점 찾기
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                cur = [i,j]
                break
                
    for r in routes:
        direction, distance = r.split(" ")
        dx,dy = m[direction]
        distance = int(distance)
        
        valid = True
        for d in range(1,distance+1):
            nx, ny = cur[0]+dx*d, cur[1]+dy*d  
            
            if not (0<=nx<len(park) and 0<=ny<len(park[0])): 
                valid = False
                break
            if park[nx][ny] == 'X':
                valid = False
                break 
        if valid:
            cur[0] += dx * distance
            cur[1] += dy * distance
    
    return cur