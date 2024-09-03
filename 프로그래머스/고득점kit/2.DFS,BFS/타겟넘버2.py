#타겟 넘버
from collections import deque

def solution(numbers, target):
    queue = deque()
    queue.append((0,0))
    answer = 0
    while queue:
        i, score = queue.popleft()
        if i >= len(numbers):
            if score == target:
                answer+=1
            continue

        queue.append((i+1,score+numbers[i]))
        queue.append((i+1,score-numbers[i]))

    return answer

print(solution([1, 1, 1, 1, 1],3))
print(solution([4, 1, 2, 1], 4))


#타겟 넘버
# from collections import deque

# def solution(numbers, target):
#     queue = deque()
#     queue.append((0,0))
#     answer = 0
#     while queue:
#         i, score = queue.popleft()
#         if i == len(numbers) and score == target:
#             answer+=1
#         else:
#             if i+1 <= len(numbers):
#                 queue.append((i+1,score+numbers[i]))
#                 queue.append((i+1,score-numbers[i]))

#     return answer