from collections import Counter

string = list(input())
string_count = Counter(string)

# 홀수 개수의 문자가 두 개 이상이면 회문을 만들 수 없음
odd_count = sum(1 for count in string_count.values() if count % 2 != 0)
if odd_count > 1:
    print("I'm Sorry Hansoo")
else:
    half_palindrome = []
    middle_char = ''

    for char, count in sorted(string_count.items()):
        if count % 2 != 0:
            middle_char = char
        half_palindrome.append(char * (count // 2))

    half_palindrome = ''.join(half_palindrome)
    palindrome = half_palindrome + middle_char + half_palindrome[::-1]
    print(palindrome)