#https://hongcoding.tistory.com/56
from itertools import combinations
from bisect import bisect_left


def solution(info, query):
    answer = []
    DB = {}

    for i in info:
        infol = i.split()  # info안의 문자열을 공백을 기준으로 분리
        mykey = infol[:-1]  # info의 점수제외부분을 key로 분류
        myval = infol[-1]  # info의 점수부분을 value로 분류

        for j in range(5):  # key들로 만들 수 있는 모든 조합 생성
            for c in combinations(mykey, j):
                tmp = ''.join(c) #keyinfo들을 문자열로 합침
                if tmp in DB:
                    DB[tmp].append(int(myval))  # 그 조합의 key값에 점수 추가
                else:
                    DB[tmp] = [int(myval)]

    for k in DB:
        DB[k].sort()  # value 값을 기준으로 점수순으로 정렬

    for qu in query:  # query도 마찬가지로 key와 value로 분리
        myqu = qu.split()
        qu_key = myqu[:-1]
        qu_val = myqu[-1]

        while 'and' in qu_key:  # and 제거
            qu_key.remove('and')
        while '-' in qu_key:  # - 제거
            qu_key.remove('-')
            
        qu_key = ''.join(qu_key)  # dict의 key처럼 문자열로 변경

        if qu_key in DB:  # query의 key가 DB의 key로 존재하면
            scores = DB[qu_key] #DB의 value들을 가져온다
            if scores:  # score리스트에 값이 존재하면
                #가져온 점수값에서 기준 점수값을 넘는 것들의 개수를 이분탐색을 통해 구한다.
                enter = bisect_left(scores, int(qu_val))#bisect_left: score라는 정렬된 배열이 있을 때, quval이라는 새로운 수를 추가하고 싶을 때 어떤 인덱스에 넣어야하는지 알려줌
                answer.append(len(scores) - enter)
        else:
            answer.append(0)

    return answer