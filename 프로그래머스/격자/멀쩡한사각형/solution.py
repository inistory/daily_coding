# def gcd(a,b):
#     return b if a==0 else gcd((b%a),a)

# def solution(w,h):
#     return w*h -w -h +gcd(w,h)

import math

def solution(w,h):
    return w*h -w -h +math.gcd(w,h)