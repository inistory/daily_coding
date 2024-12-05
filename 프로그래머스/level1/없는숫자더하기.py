def solution(numbers):
    answer = [i for i in range(0,10)]
    for num in numbers:
        if num in answer:
            answer.remove(num)
    return sum(answer)