import sys

input = sys.stdin.read
data = input().split()
v = ['a','e','i','o','u']

def has_three_consecutive(word):
    vowels = set(v)
    count = 0
    last_char_type = None
    
    for char in word:
        if char in vowels:
            char_type = 'vowel'
        else:
            char_type = 'consonant'
        
        if char_type == last_char_type:
            count += 1
        else:
            count = 1
            last_char_type = char_type
        
        if count >= 3:
            return True
    
    return False

def has_two_consecutive(word):
    last_char = None
    count = 0
    for char in word:
        if last_char == char:
            count += 1
        else:
            last_char = char
            count = 1
    
        if count ==2:
            if last_char not in ['e', 'o']:
                return True
            return False
    return False
            
        
        

for word in data:
    if word == 'end':
        break
    
    if not any(w in word for w in v): #any:주어진 요건을 만족하는 요소가 있는지 확인
        print(f"<{word}> is not acceptable.")
    elif has_three_consecutive(word):
        print(f"<{word}> is not acceptable.")
    elif has_two_consecutive(word):
        print(f"<{word}> is not acceptable.")
    else:
        print(f"<{word}> is acceptable.")