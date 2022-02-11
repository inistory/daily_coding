import sys
input = sys.stdin.readline

n, m  = map(int, input().split())
money = list()

for i in range(n):
    money.append(int(input()))

#money를 가지고 m원을 만들 때, 만들기 위한 최소한의 화폐 개수
if m > min(money):
    print(-1)
if