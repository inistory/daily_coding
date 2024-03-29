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
                    
                
        
    
    
    