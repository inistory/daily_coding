S = str(input())

cnt = set()

for i in range(0, len(S)):
    for j in range(i+1, len(S)+1):
        cnt.add(S[i:j])
print(len(cnt))