import sys
input = sys.stdin.readline
N, M = map(int, input().split())
num_to_name = {}
name_to_num = {}
for i in range(N):
    name = input().strip()
    num_to_name[str(i+1)] = name
    name_to_num[name] = str(i+1)

for j in range(M):
    quiz = input().strip()
    if quiz.isdigit():
        print(num_to_name[quiz])
    else:
        print(name_to_num[quiz])