n, d = map(int,input().split()) 
nl = [i for i in range(1,n+1)] 
answer = [] 
num = 0 
while len(answer) != n: # nl : 1,2,3,4,5,6,7,8,9,10 4 // 4 8 3 7 
    num = (num + (d-1)) % len(nl) 
    answer.append(nl.pop(num)) 
print("<%s>" % (", ".join(map(str,answer))))
