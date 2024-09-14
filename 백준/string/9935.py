#문자열 폭발
# string = str(input())
# p = str(input())
    
# while p in string:
#     string = string.replace(p,'')

#     if len(string)==0:
#         break
    
# if len(string)!=0:  
#     print(string)

string = str(input())
p = str(input())
stack = []
p_len = len(p)

for s in string:
    stack.append(s)
    if ''.join(stack[-p_len:]) == p:
        del stack[-p_len:]
        
result = ''.join(stack)

if result:
    print(result)
else:
    print("FRULA")
        

