import math

def time_to_minutes(time):
    h, m = map(int, time.split(':'))
    return h*60 + m
    
def solution(fees, records):
    answer = []

    # 기본 시간, 기본 요금, 단위 시간, 단위 요금 순
    dt, df, ut, uf = fees
    
    dic = dict()

    for r in records:
        time, car, inout = r.split()
        car = int(car)
        
        if car in dic: #차별로 주차시간(분단위), inout을 저장
            dic[car].append([time_to_minutes(time), inout])
        else:
            dic[car] = [[time_to_minutes(time), inout]]
    
    rList = sorted(dic.items()) #key를 기준으로 딕셔너리를 오름차순 정렬해서 리스트로 반환

    for r in rList:
        t = 0

        for rr in r[1]: #item들 확인 
            if rr[1] == "IN": #inout가 IN이면
                t -= rr[0] #시간 빼기
            else: #OUT 이면
                t += rr[0] #시간 더하기
        
        if r[1][-1][1] == "IN": #마지막에 출차 내역이 없는 경우
            t += time_to_minutes('23:59') #출차시간을 23:59으로 간주
        
        if t <= dt: #기본시간보다 작으면 기본요금을 추가
            answer.append(df)
        else: #기본 시간이상이면
            answer.append(df + math.ceil((t-dt) / ut) * uf)        

    return answer