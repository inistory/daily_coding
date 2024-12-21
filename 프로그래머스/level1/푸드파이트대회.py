def solution(food):
    answer = ''
    for i, food in enumerate(food):
        if i!=0 and food%2==0: #짝수
            for _ in range(int(food/2)):
                answer+=str(i)
        elif i!=0 and food%2!=0:
            for _ in range(int((food-1)/2)):
                answer+=str(i)
    
    answer_f = answer
    answer_f+='0'
    answer_f+=answer[::-1]
    return answer_f