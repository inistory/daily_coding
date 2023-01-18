#정확성테스트9,10, 효율성테스트 X
def solution(stones, k):
    answer = 0
    zero = 0
    complete = 0
    check = True
    while check:
        # print(stones)
        for i, stone in enumerate(stones):
            if stone == 0: #연속으로 0이 몇번 나오는지
                zero+=1
            else: #숫자가 나오면
                stones[i] -=1
                zero = 0 #원상복귀
                
            #건널수 있는지 없는 검사
            if zero >= k:
                check = False
                break
        if check:
            complete+=1
        
    # print(complete)
    return complete
    # return answer