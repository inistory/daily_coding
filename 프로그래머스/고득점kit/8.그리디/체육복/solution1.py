def solution(n, lost, reserve):
    answer = []
    #체육복을 잃어버린 학생 중 여벌이 없는 학생 =참가불가
    set_lost = set(lost)-set(reserve)
    #체육복 여벌이 있던 학생 중 잃어버린 학생빼고 =빌려줄수있는 학생
    set_reserve = set(reserve)-set(lost)

    #참가 가능한 학생 중
    for i in set_reserve:# 그 왼쪽이 체육복이 없는 경우
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost: #그 오른쪽이 없는 경우
            set_lost.remove(i+1) 
    answer = n-len(set_lost)
    return answer