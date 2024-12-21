def solution(s, n):
    result = ''
    for char in s:
        if char.islower():  
            #ord: 문자 -> 아스키코드
            #chr: 아스키코드 -> 문자
            #26: 알파벳은 26개, 순환되게 나누어주기
            result += chr((ord(char) - ord('a') + n) % 26 + ord('a'))
        elif char.isupper():  
            result += chr((ord(char) - ord('A') + n) % 26 + ord('A'))
        else:  # 공백 처리
            result += char
    return result