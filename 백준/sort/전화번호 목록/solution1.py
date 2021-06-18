import sys
def solution(numbers):
    numbers.sort() #numbers 정렬시키면 사전순으로 정렬
    for i in range(len(numbers)-1): #정렬되어있으므로 i번째와 i+1번째만 비교해보면됌
        if numbers[i] in numbers[i+1]: 
            return False
    return True

numbers=[]
t=int(input())
answer=[]
for i in range(t):
    n=int(input())
    for _ in range(n):
        numbers.append(sys.stdin.readline().strip())
    answer.append(solution(numbers))
    numbers.clear()
for yn in answer:
    if yn == False:
        print('NO')
    else:
        print('YES')