def solution(numbers):
    numbers = list(map(str,numbers))
    numbers.sort(key=cmp, reverse = True)
    return str(int(''.join(numbers))) #모든 값이 0000일때는 0으로 바꿔줘야해서 int 다음 str

def cmp(x):
    for i in range(5):
        x += x
    return x[:5]