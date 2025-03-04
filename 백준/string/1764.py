n, m = map(int,input().split())

l_set = {input() for _ in range(n)}
s_set = {input() for _ in range(m)}

answer_list = list(l_set & s_set)
answer_list.sort()

print(len(answer_list))
for name in answer_list:
    print(name)
