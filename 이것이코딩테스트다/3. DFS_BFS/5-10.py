#가로, 세로 길이를 공백기준으로 구분하여 입력받기 
n, m = map(int, input().split())

#2차원 리스트로 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x,y):
    #주어진 가로, 세로 범위를 벗어나는 경우에 종료
    if x <=-1 or x>=n or y<=-1 or y>=m:
        return False
    
    if graph [x][y] == 0: #아직 방문처리 하지 않았다면
        graph[x][y] = 1  #방문처리

        #상하좌우 재귀
        dfs(x-1, y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True #상하좌우에 0들을 모두 방문한 후
    return False #1만 있으면 False리턴

result = 0
for i in range(n):
    for j in range(m):
        #현재 위치에서 dfs 수행
        if dfs(i,j) == True: #아이스크림이 만들어졌다면
            result +=1 #카운트
           
print(result)

#dfs는 한꺼번에 방문처리하는 용도로 사용