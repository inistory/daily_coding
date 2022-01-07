## 1. 문제 설명

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/42579)

- genres : 노래의 장르를 나타내는 문자열 배열
- plays : 노래별 재생 횟수를 나타내는 정수 배열
- return : 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로
- 규칙

1. 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
2. 장르 내에서 많이 재생된 노래를 먼저 수록합니다.

## 2. 코드

```python
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
```

## 3. 어려웠던 점

- 딕셔너리를 리스트에 append하는 과정에서 같은 값이 들어가서 당황했는데, 딕셔너리의 특성상 바뀐 내용을 그대로 가져와서 그런거였다. for문안에서 딕셔너리를 초기화하여 해결했다.
- 장르별로 가장 많이 재생된 노래를 두개씩만 모아야하는데 그 조건을 나중에 봤다.
