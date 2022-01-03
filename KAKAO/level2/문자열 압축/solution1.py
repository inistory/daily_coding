def solution(s):
    answer = len(s)
    for i in range(1,int(len(s))+1): #몇개씩 자를지
        pos = 0 #현재위치
        #단위 설정
        length = len(s)
        while pos + i <=len(s):
            unit = s[pos:pos+i]
            pos+=i #i만큼 증가시키기
            
            #단위가 몇번 등장하는지 찾기
            count =0
            while pos + i  <= len(s):
                if s[pos:pos+i] == unit:
                    count+=1
                    pos +=i
                else:
                    break
            if count>0:
                #감소할 문자열 길이
                length -=i*count 
                #증가할 숫자길이 (등장횟수)
                if count<9: 
                    length+=1
                elif count < 99:
                    length+=2
                elif count < 999: 
                    length+=3
                else: #s의 길이가 1000일 경우
                    length+=4 
        answer = min(answer, length)
    return answer
        