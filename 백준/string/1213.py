# 팰린드롬 만들기
name = str(input())
name_count = {}

# 각 문자의 등장 횟수를 세기
for n in name:
    if n not in name_count:
        name_count[n] = 1
    else:
        name_count[n] += 1

# 홀수 개수의 문자가 몇 개인지 확인
odd_count = sum(1 for value in name_count.values() if value % 2 != 0)

# 홀수 개수의 문자가 1개를 초과하면 팰린드롬 불가능
if odd_count > 1:
    print("I'm Sorry Hansoo")
else:
    temp = []
    middle_char = ''
    for key, item in sorted(name_count.items()):  # 사전순
        if item % 2 != 0:
            middle_char = key
        for _ in range(item // 2):
            temp.append(key)

    half_str = ''.join(temp)
    palindrome = half_str + middle_char + half_str[::-1]
    print(palindrome)
    
    
# 팰린드롬 만들기 (chatgpt)

def make_palindrome(name):
    from collections import Counter #이런게 있다니..

    # 문자 개수 세기
    count = Counter(name)
    
    # 홀수 개수의 문자가 몇 개인지 확인
    odd_count = sum(1 for v in count.values() if v % 2 != 0)
    
    # 홀수 개수의 문자가 1개를 초과하면 팰린드롬 불가능
    if odd_count > 1:
        return "I'm Sorry Hansoo"
    
    # 팰린드롬의 절반을 만들기 위한 리스트
    half_palindrome = []
    middle_char = ''
    
    for char, cnt in sorted(count.items()):
        if cnt % 2 != 0:
            middle_char = char
        half_palindrome.extend(char * (cnt // 2)) #extend는 잘 몰랐는데 익혀두자
    
    # 절반을 뒤집어서 팰린드롬 완성
    half_palindrome = ''.join(half_palindrome)
    return half_palindrome + middle_char + half_palindrome[::-1]

# 입력 받기
name = input().strip()

# 결과 출력
print(make_palindrome(name))