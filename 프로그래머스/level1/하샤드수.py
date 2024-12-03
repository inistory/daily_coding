def solution(x):
    temp = 0
    for i in list(str(x)):
        temp+=int(i)
    
    if x%temp == 0:
        return True
    else:
        return False