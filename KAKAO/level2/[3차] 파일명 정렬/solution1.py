from functools import cmp_to_key

def compare(s1,s2):
    head1, number1, tail1 = s1[0], s1[1], s1[2]
    head2, number2, tail2 = s2[0], s2[1], s2[2]

    head1, head2 = head1.upper(), head2.upper() #알바벳 구분 없으니까
    number1, number2 = int(number1), int(number2) #비교를 위해 int화

    if head1 != head2:
        return -1 if head1 < head2 else 1 #만약 head1이 head2보다 작으면 교환(-1)
    else: #head1 == head2
        return number1 - number2 if number1 != number2 else 1 #숫자가 서로 같지 않을 때만 빼기(둘이 같을 때 0이니까 교환이 되어버림을 방지)

def split_fname(filename):
    HEAD = ""
    NUMBER = ""
    TAIL = ""
    i = 0
    while not filename[i].isnumeric():
        i+=1
    HEAD = filename[:i]

    j = i
    while filename[j].isnumeric():
        j+=1
        if j == len(filename): #TAIL이 없는 경우
            NUMBER = filename[i:j]
            return [HEAD, NUMBER, '']

    NUMBER = filename[i:j]
    TAIL = filename[j:]

    return [HEAD, NUMBER,TAIL]


def solution(files):
    answer = []
    filenames  = []
    for file in files: #파일명 하나씩 조회
        filenames.append(split_fname(file))

    filenames.sort(key=cmp_to_key(compare))

    for i, filename in enumerate(filenames):
        filenames[i] = ''.join(filename)
    return filenames