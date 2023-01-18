## 1. 문제 설명

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/17677)

- 입력 : 문자열 두 개
- 출력 : 자카드 유사도 : 문자열을 두개씩 끊어서 집합을 각각 만들고, 두 집합의 교집합길이/합집합길이

## 2. 코드

```python
def solution(str1, str2):
    strings = []
    for string in [str1,str2]:
        conv = string.lower()
        convs = {}
        for i in range(0, len(conv)-1):
            word = conv[i:i+2]
            if word.isalpha(): #알파벳이면
                convs[word] = convs.get(word,0)+1 #word라는 key값 있으면 그 값을 받아와서 그 값에 +1, 없으면 0을 넣어줌
        strings.append(convs)


    str1, str2 = strings
    intersection = [] #교집합
    for s1 in str1:
        if s1 in str2:
            intersection+=[s1 for _ in range(min(str1[s1],str2[s1]))]

    union = [] #합집합
    jaccard_keys = list(str1.keys())+list(str2.keys())

    for j in set(jaccard_keys):
        #max(str1[j],str2[j])은 해당 키워드가 한쪽에서없으면 에러가 나서 없는 경우를 0으로 채워주는 코드로 대체
        union += [j for _ in range(max(str1.get(j,0),str2.get(j,0)))]

    n = len(intersection) / len(union) if len(union)!=0 else 1
    return int(n * 65536)

```

## 3. 회고

-

## 4. 참고

https://www.youtube.com/watch?v=nbrKZzwsQmg&list=PLSK4WsJ8JS4c1aMT5sZp2Nf50g2WhQuro
