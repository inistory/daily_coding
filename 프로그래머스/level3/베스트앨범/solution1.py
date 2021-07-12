def solution(genres, plays):
    n = len(genres)
    play_count = {}
    #장르별 재생 수
    for i in range(n):
        if genres[i] in play_count:
            play_count[genres[i]] += plays[i]
        else:
            play_count[genres[i]] = plays[i]
            
        
    hash_table = []
    for i in range(n):
        temp = {}
        temp['index'] = i
        temp['genres'] = genres[i]
        temp['plays'] = plays[i]
        temp['play_count'] = play_count[genres[i]]
        hash_table.append(temp)
    
    #속한 노래가 많이 재생된 장르를 먼저 수록
    #장르 내에서 많이 재생된 노래를 먼저 수록합니다.

    answer = sorted(hash_table, key = lambda x : (-x['play_count'], -x['plays']))
    check = {} #장르 두개 제한하기 위한 딕셔너리
    for key in list(play_count.keys()):
        check[key] = 0
        
    final = []
    for ans in answer:
        if check[ans["genres"]] < 2:
            check[ans["genres"]] += 1
            print(check)
            final.append(ans["index"])
    return final