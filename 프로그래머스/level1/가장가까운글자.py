def solution(s):
    last_seen = {}# 각 문자의 마지막으로 등장한 인덱스를 저장할 딕셔너리
    answer = []
    
    for i, char in enumerate(s):
        # 현재 문자가 이전에 등장했는지 확인
        if char in last_seen:
            # 이전에 등장했다면, 현재 인덱스와 이전 인덱스의 차이를 결과 리스트에 추가
            answer.append(i - last_seen[char])
        else:# 이전에 등장하지 않았다면, -1을 결과 리스트에 추가
            answer.append(-1)
        last_seen[char] = i # 현재 문자의 인덱스를 딕셔너리에 업데이트
    
    return answer