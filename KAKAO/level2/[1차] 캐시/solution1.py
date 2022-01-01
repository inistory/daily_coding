def solution(cacheSize, cities):
    cache = []
    time = 0

    for city in cities:
        city = city.lower() #도시이름의 대소문자 구분 x
        if city in cache:
            time +=1
            cache.remove(city) #기존 캐시 제거
            cache.append(city) #새롭게 캐시 넣어줌
        else:
            time +=5
            if cacheSize!=0:
                if len(cache) >= cacheSize: #새로운 캐시를 넣을 수 없는 상황이라면
                    cache.pop(0) #가장 오래된 아이템 삭제
                cache.append(city) #이번에 넣어야할 아이템을 캐시에 추가
            
    return time