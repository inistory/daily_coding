N = int(input())

arr = list(map(int,input().split()))
stack = []
curr = 1

for a in arr:
    while stack and stack[-1] == curr:
        stack.pop()
        curr+=1
    if a == curr:
        curr+=1
    else:
        stack.append(a)

while stack and stack[-1] == curr:
    stack.pop()
    curr+=1

if not stack:
    print('Nice')
else:
    print('Sad')