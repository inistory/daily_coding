#사탕 게임
n = int(input())
graph = [list(input()) for _ in range(n)]

#가장 긴 연속 부분 행렬 찾기
def check(graph):
    max_length = 1
    #행 확인
    for i in range(n):
        count = 1
        for j in range(1,n):
            if graph[i][j] == graph[i][j-1]:# 이전값과 같으면
                count+=1
                max_length = max(max_length,count)
            else:
                count = 1
    
    #열 확인             
    for j in range(n):
        count = 1  
        for i in range(1,n):
            if graph[i][j] == graph[i-1][j]:
                count+=1
                max_length = max(max_length,count)
            else:
                count = 1           
    
    return max_length     
            
answer = 0
for i in range(n):
    for j in range(n):
        if j+1 <n and graph[i][j] != graph[i][j+1] :
                graph[i][j], graph[i][j+1] = graph[i][j+1], graph[i][j]
                answer = max(answer,check(graph))
                graph[i][j], graph[i][j+1] = graph[i][j+1], graph[i][j]
            
        if i+1 < n and graph[i][j] != graph[i+1][j]:
                graph[i][j], graph[i+1][j] = graph[i+1][j], graph[i][j]
                answer = max(answer,check(graph))
                graph[i][j], graph[i+1][j] = graph[i+1][j], graph[i][j]          
 
print(answer)