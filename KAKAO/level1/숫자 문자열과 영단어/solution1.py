def solution(S):
    num_dic = {'zero':'0','one':'1', 'two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    value_list = num_dic.values()
    result = []
    temp = ''
    for i,s in enumerate(S):
        #만약 숫자가 나오면 숫자를 append
        if s in value_list:
            result.append(s)
        #문자가 나오면 
        else:
            temp +=s #key에 문자가 존재하면 임시 문자열에 계속 붙이다가
            if temp in num_dic: #num_dic의 key에 만들어진 임시문자열과 같은게 있으면 
                result.append(num_dic[temp])
                temp = '' #temp를 초기화
                
    return int(''.join(result)) #리스트 -> 문자열 -> 숫자