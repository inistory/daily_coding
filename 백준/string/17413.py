# 단어 뒤집기2

string = input()

result = []
word = ''
inside_tag = False

for char in string:
    if char == '<':
        if word:
            result.append(word[::-1])
            word = ''
        inside_tag = True
        result.append(char)
    elif char == '>':
        inside_tag = False
        result.append(char)
    elif inside_tag:
        result.append(char)
    else:
        if char == ' ':
            result.append(word[::-1])
            result.append(char)
            word = ''
        else:
            word += char

if word:
    result.append(word[::-1])

print(''.join(result))