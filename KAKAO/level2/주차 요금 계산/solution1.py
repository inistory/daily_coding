#처음에 풀다가 망한코드
import math

#자동차별 주차시간 계산
def get_time(records):
    info = {re.split(" ")[1]:[0,"23:59",0]  for re in records} #차번호:[IN, OUT, 내야할 요금]
    # print(info)
    for rec in records:
        r = rec.split(" ")#공백기준으로 자르기
        if r[2] == 'IN':
            info[r[1]][0] = r[0]
        else:
            info[r[1]][1] = r[0]
    # print(info)
    return info

#요금 계산하는 함수
def get_price(fees, info): #기본 요금인지여부, 주차시간
    #info에 마지막요소에 요금을 추가
    #요금 개선
    print(info)
    for car, inf in info.items():#자동차별로 시간을 확인
        IN_hour, IN_min = int(inf[0].split(":")[0]),int(inf[0].split(":")[1])  
        OUT_hour, OUT_min = int(inf[1].split(":")[0]),int(inf[1].split(":")[1])  
        print(IN_hour,IN_min)
        print(OUT_hour,OUT_min)
        time = (OUT_hour - IN_hour)*60 + OUT_min - IN_min #누적시간
        print(time)
        basic = fees[0] #기본요금
    #     if time <= basic:
    #         info[car][2] = time
    #     else:
    #         if  (time - fees[1]) % fees[2] !=0: #나누어
    #         #기본 요금 + (누적시간 - 기본시간) / 단위시간 * 단위요금
    #             info[car][2] = basic + math.ceil((time - fees[1]) /fees[2]) * fees[3] 
    #         else:
    #             info[car][2] = basic + (time - fees[1]) /fees[2] * fees[3] 
    # return info

def solution(fees, records):
    answer = []
    info = get_time(records) 
    # print(get_price(fees,info))
    result = get_price(fees,info)
    #차량번호 작은 순으로 정렬(오름차순)
    # sorted_dict = sorted(result.items(), key = lambda item: item[0], reverse = False)
    # # print(sorted_dict)
    # #anwer에 담기
    # for sd in sorted_dict:
    #     answer.append(sd[1][2]) 
    # print(answer)