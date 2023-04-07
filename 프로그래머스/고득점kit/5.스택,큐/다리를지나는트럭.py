import math
def solution(bridge_length, weight, truck_weights):
    time = 0 #걸린시간
    queue = [0 for _ in range(bridge_length)] #다리를 건너는 트럭 현황
    
    while len(queue)!=0: #다리에 트럭이 없어질때까지
        time += 1
        queue.pop(0) #지나간 트럭은 빼기
        if truck_weights: #대기 트럭이 존재하면
            if sum(queue) + truck_weights[0] <= weight:#추가트럭이 다리에 올라갈수있으면
                queue.append(truck_weights.pop(0))
            else:
                queue.append(0)
    
    return time