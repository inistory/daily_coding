# - `n × n` 크기의 별 패턴을 만들어주는 함수.
# - 결과는 **문자열 리스트**로 반환해. (예: `['***', '* *', '***']`)
def draw_star(n):
    if n == 1:#1×1 크기의 별 패턴은 그냥 ['*']
        return ['*']
    
    stars = draw_star(n // 3)#더 작은 패턴을 만듦
    result = []

    for line in stars:#상단블록
        result.append(line * 3)
    for line in stars: #중간블록
        result.append(line + ' ' * (n // 3) + line)
    for line in stars:#하단블록
        result.append(line * 3)

    return result

N = int(input())
output = draw_star(N)
for line in output:
    print(line)
