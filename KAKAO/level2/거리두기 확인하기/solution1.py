
import queue

D = ((-1,0),(1,0),(0,-1),(0,1))#상하좌우로 이동하기 위한 delta array

def bfs(place, row, col): #P의 위치에서 bfs실행
    visited = [[False for _ in range(5)] for _ in range(5)] #5x5
    q = queue.Queue()
    visited[row][col] = True #큐 꺼내기전에 마킹
    q.put((row,col,0)) #행, 열, 거리

    while not q.empty():
        curr = q.get()

        if curr[2] > 2: #거리가 2를 초과하면 스킵 
            continue
        if curr[2] !=0 and place[curr[0]][curr[1]] == 'P': #시작위치가 아닌 다른 P를 만났을 때
            return False
        
        #길이 2이하일 때
        for i in range(4):
            nr = curr[0] +D[i][0]
            nc = curr[1] +D[i][1]
            if nr < 0 or nr >4 or nc <0 or nc >4:#범위를 벗어난다면
                continue
            if visited[nr][nc]: #이미 큐에 넣은 적이 있다면 다시 넣을 필요가없음
                continue
            if place[nr][nc] == 'X':#파티션이 있으면 이동할 수 없음
                continue
            visited[nr][nc] = True
            q.put((nr,nc, curr[2]+1))
    return True


def check(place):
    for r in range(5):
        for c in range(5):
            if place[r][c] == 'P':
                if bfs(place,r,c) == False: #거리두기 안지켜짐
                    return False
    return True #조건문에 걸리지 않아서 모두 탐색을 완료하게 된다면 True 리턴


def solution(places):
    answer = []

    for place in places:
        if check(place): #거리두기를 지키고 있는지
            answer.append(1)
        else:
            answer.append(0)

    return answer