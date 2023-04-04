from collections import deque

def solution(begin, target, words):
    def bfs(begin,cnt):
        q = deque()
        q.append((begin,cnt))
    
        while q:
            cw, cnt = q.popleft()

            if cw == target:
                return cnt

            for word in words:
                same = 0
                for i in range(len(cw)):
                    if cw[i] != word[i]:
                        same+=1

                if same == 1:
                    q.append((word,cnt+1))
    answer = 0
    if target not in words:
        return 0
    else:
        answer = bfs(begin,0)
    return answer