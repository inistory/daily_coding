## 1. 문제 설명

[문제 링크](https://programmers.co.kr/learn/courses/30/lessons/67256)

- 입력 :

  - numbers [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5] : 누를 번호를 순서대로
  - hand "right" : 오른손잡이인지, 왼손잡이인지

- 출력 :
  - "LRLLLRLLRRL"
  - 1,4,7 은 왼손으로 누르고, 3,6,9는 오른손으로 누른다.
  - 그리고 나머지 숫자들은 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용
  - 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용
  - 각 번호(numbers)를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return

## 2. 코드

solution1.py

```python
def check_near_hand(current_position,num):
    positions = {
        1:(0,0),2:(0,1),3:(0,2),
        4:(1,0),5:(1,1),6:(1,2),
        7:(2,0),8:(2,1),9:(2,2),
        '*':(3,0),0:(3,1),'#':(3,2)
    }

    left_hand = positions[current_position[0]]
    right_hand = positions[current_position[1]]
    num_position = positions[num]
    #왼손과 Num의 거리
    left_distance = abs(left_hand[0] - num_position[0]) + abs(left_hand[1]-num_position[1])
    #오른손과 Num의 거리
    right_distance = abs(right_hand[0] - num_position[0]) + abs(right_hand[1]-num_position[1])

    if left_distance < right_distance:
        return 'L'
    elif left_distance > right_distance:
        return 'R'
    else:
        return 'hand'

def solution(numbers, hand):
    answer = ''
    current_position = ['*','#']

    left_key = [1,4,7]
    right_key = [3,6,9]

    for num in numbers:
        if num in left_key:
            current_position[0] = num
            answer +='L'
        elif num in right_key:
            current_position[1] = num
            answer +='R'
        else:
            if check_near_hand(current_position,num) == 'L':
                current_position[0] = num
                answer +='L'
            elif check_near_hand(current_position,num) == 'R':
                current_position[1] = num
                answer +='R'
            else:
                if hand == 'left':
                    current_position[0] = num
                    answer +='L'
                else:
                    current_position[1] = num
                    answer +='R'
    return answer

```

solution2.py

```python
def check_near_hand(l,r,num, hand):
    positions = {
        1:(0,0),2:(0,1),3:(0,2),
        4:(1,0),5:(1,1),6:(1,2),
        7:(2,0),8:(2,1),9:(2,2),
        '*':(3,0),0:(3,1),'#':(3,2)
    }

    left_distance = abs(positions[l][0] - positions[num][0]) + abs(positions[l][1]-positions[num][1])
    right_distance = abs(positions[r][0] - positions[num][0]) + abs(positions[r][1]-positions[num][1])

    if left_distance == right_distance:
        return 'L' if hand == 'left' else 'R'
    return 'L' if left_distance < right_distance else 'R'


def solution(numbers, hand):
    answer = ''
    current_position = ['*','#']

    left_key = [1,4,7]
    right_key = [3,6,9]

    for num in numbers:
        if num in left_key:
            current_position[0] = num
            answer +='L'
        elif num in right_key:
            current_position[1] = num
            answer +='R'
        else:
            if check_near_hand(current_position[0],current_position[1],num,hand) == 'L':
                current_position[0] = num
                answer +='L'
            else:
                current_position[1] = num
                answer +='R'

    return answer

```

## 3. 회고

- 거리계산을 어떻게 할 지가 가장 고민이었다.
- 딕셔너리로 좌표를 정해주고 abs(왼손 현재위치 x값 - 누르려는 번호위치 x값) + abs(왼손 현재위치 y값 - 누르려는 번호위치 y값) 으로 왼손과 누르려는 번호의 거리, 오른손도 마친가지로 해서 둘을 비교했다.
- 첫 번째 풀이에서는 거리계산 과정에서 헷갈려서 여러 변수를 지정하여 썼다.
- 그래서 두 번째 풀이에서는 current_position 배열 자체보다 왼손현재위치, 오른손현재위치를 따로 매개변수로 전달했다.
- 두 번째 풀이는 if 문이 너무 많이 쓰인 것 같아서 한줄로 정리했다.
- 알고리즘이 문제에 적혀있어서 이를 바탕으로 큰 틀을 잡고 필요한 함수를 나중에 작성해나가는 것으로 방향을 잡은 것이 도움이 되었다.
