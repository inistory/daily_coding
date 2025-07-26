import math

a,b = map(int, input().split())
c,d = map(int, input().split())

lcm = math.lcm(b,d)

j = a*(lcm//b) + c*(lcm//d)
m = lcm

gcd = math.gcd(j,m)

print(j//gcd, m//gcd)
