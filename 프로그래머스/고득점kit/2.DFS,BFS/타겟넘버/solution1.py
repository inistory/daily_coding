answer = 0
def dfs(numbers, target, length, i):
    global answer
    if i == len(numbers): #인덱스 i가 numbers의 길이인 length와 같다면
        if (sum(numbers)) == target: #numbers의 값이 target과 같은지 확인하고
            answer += 1 #같다면 answer의 값을 1 증가킨다.
            return  
    else:
        dfs(numbers, target, length, i+1) #그렇지 않다면, dfs(numbers, target, length, i+1)을 호출한 뒤
        #numbers[i]의 값에 -1을 곱한 채로 dfs(numbers,target, length, i+1)을 호출한다. 
        numbers[i] *= -1
        dfs(numbers, target, length, i+1)


def solution(numbers, target):
    global answer
    length = len(numbers)
    dfs(numbers, target, length, 0)#dfs(numbers, target, length, 0)을 호출한다.

    return answer