def solution(ingredient):
    stack = []
    burger = [1,2,3,1]
    count = 0
    
    for i in ingredient:
        stack.append(i)
        
        if stack[-4:] == burger:
            count+=1
            del stack[-4:]
    
    return count