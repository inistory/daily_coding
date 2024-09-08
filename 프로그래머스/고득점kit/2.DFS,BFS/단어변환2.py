from collections import deque
def solution(begin, target, words):
    n = len(words)
    if target not in words:
        return 0
    def check(word,curr):
        cnt = 0 
        for i in range(len(word)):
            if curr[i] == word[i]:
                cnt+=1
        return cnt                   
        
    queue = deque()
    queue.append((begin,0))

    while queue:
        curr,count = queue.popleft()    
        if curr == target:
            return count
        for i in range(n):
            if check(words[i],curr)==len(curr)-1 and check(words[i], target)>0:
                queue.append((words[i],count+1))
    return count
    