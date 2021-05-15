def solution(nums):
    answer = 0
    max_num = len(nums)/2
    temp = [] #지금까지 나온 포켓몬 저장
    for i in range(len(nums)):
        if not nums[i] in temp:
            temp.append(nums[i])
        if len(temp) == max_num:
            break
    return len(temp)