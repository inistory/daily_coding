def solution(citations):
    answer = 0
    citations.sort()  
    for i in range(1,len(citations)+1): #h후보: 1 ~ 5 각각 h-index가 되는지확인
        min_num = citations[-i] 
        if min_num >= i:  #i번째 논문의 인용수가 i보다 크면 i번째 ~ len(citationtion)번째 까지는 모두 hindex 만족
            answer = i #계속 더 큰 값으로 업데이트 됨

    return answer


# [0,1,3,5,6] -> 갯수에 해당
# [1,2,3,4,5] -> h후보 인덱스