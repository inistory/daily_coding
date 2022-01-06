import re

db = {'S':'**1', 'D':'**2','T':'**3','#':'*-1'}
def solution(dartResult):
    answer =''
    #dartResult에서 '[SDT][*#]?'이런 패턴을 찾으면 '\g<1> ' 바꿔주겠다.
    # -> 한 점수마다 그룹화해서 공백을 붙여줌
    for i in re.sub('([SDT][*#]?)', '\g<1> ',dartResult).split():
        #'*'처리
        if i[-1] == '*': #현재 점수의 마지막에 *이 있다면
            if answer: #이전 점수가 있는지 확인
                answer = answer[:-1] + '*2+' #이전 점수의 마지막 부호인 +를 빼고 *2+로 대체
            i+='2'#현재 점수 뒤에는 항상 2를 붙이기 -> *2가됨
        #*를 제외한 다른 문제 replace
        for j in db.keys():
            i = i.replace(j,db[j])
        answer+= i + '+'
    return eval(answer[:-1]) #마지막에 있는 + 기호는 지운채로 eval적용해야함