def solution(genres, plays):
    n = len(genres)
    play_count = {} #장르별 총 재생횟수
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
        temp['play_count'] = play_count[genres[i]] #장르별 총 재생횟수
        hash_table.append(temp)
    
    #1)속한 노래가 많이 재생된 장르를 먼저 수록, 2)장르 내에서 많이 재생된 노래를 먼저 수록
    answer = sorted(hash_table, key = lambda x : (-x['play_count'], -x['plays']))
    check = {} #장르 갯수를 제한하기 위한 딕셔너리
    for key in list(play_count.keys()):
        check[key] = 0
        
    final = []
    for ans in answer:
        if check[ans["genres"]] < 2:#장르별 갯수 두개까지로 제한
            check[ans["genres"]] += 1
            final.append(ans["index"])
    return final