N = int(input())
stars = [[0 for i in range(N)] for i in range(N)] #별 존재여부 저장

def fill_star(N, x, y) :
    if N ==1: #종료 조건
        stars[y][x] = '*'
    else:
        next_size = N //3
        for dy in range(3):
            for dx in range(3):
                if dy!=1 or dx!=1: #stars[1][1]에는 항상 별이 있어야함
                    fill_star(next_size, x + next_size*dx, y + next_size*dy) #좌측상단좌표전달


fill_star(N, 0,0)

for row in stars:
    for col in row:
        if col == '*':
            print("*", end="")
        else:
            print(" ", end="")
    print("")
