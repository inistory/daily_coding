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
