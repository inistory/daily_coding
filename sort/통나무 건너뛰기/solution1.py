T=int(input()) 
for i in range(T): 
    N=int(input()) 
    t=list(map(int,input().split())) 
    t.sort() 
    result=0 
    for j in range(2, N): 
        result=max(result,abs(t[j]-t[j-2])) 
    print(result)
