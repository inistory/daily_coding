#그룹 단어 체커
n = int(input())
answer = 0
def check(word):
    visited = {}
    for i,w in enumerate(word):
        if w not in visited:
            visited[w] = i   
        else:
            if visited[w] != i-1: 
                return 0
            else:
                visited[w] = i
    
    return 1    
for _ in range(n):
    word = str(input())
    answer +=check(word)
    
print(answer)
