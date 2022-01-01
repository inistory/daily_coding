from itertools import combinations



def solution(orders, course):
    answer = []
    foodMap = [{} for _ in range(11)] #메뉴 개수에 따라 딕셔너리를 사용(2~10까지 11개사용)
    maxCnt = [0 for _ in range(11)] #메뉴 개수별 최대등장횟수 저장 

    for str in orders:
        for num in range(2,len(str)+1): #코스를 구성하는 메뉴의 갯수는 두개 이상, 문자열 길이만큼 메뉴개수를 진행 AC면 두개, CDE면 두개혹은세개
            for i in combinations(sorted(str),num): #input으로 주어지는 문자열을 sort해서 전달, 정렬된 상태로 개수(num)만큼 조합을 만들어서 튜플형태로 리스트로 반환
                key = ''.join(i)
                if key in foodMap[num]: #메뉴구성이 이미있으면
                    foodMap[num][key] +=1
                    maxCnt[num] = max(maxCnt[num],foodMap[num][key])
                else:
                    foodMap[num][key] = 1
    
    for num in course:
        for key, value in foodMap[num].items():
            if value >=2 and value == maxCnt[num]: #두개 이상인것, 최대값과 같은 모든 것
                answer.append(key)

    return sorted(answer)
