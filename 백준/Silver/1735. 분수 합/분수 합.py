A, B = map(int, input().split())
C, D = map(int, input().split())

E = A * D + B * C
F = B * D

lst = [E, F]
lst.sort

# 유클리드 호제법
while lst[1] != 0:
    [lst[0], lst[1]] = [lst[1], lst[0] % lst[1]]

# 최대 공약수로 나누면 기약분수가 되므로 최대 공약수를 찾아서 나눈다.
print(f'{E // lst[0]} {F // lst[0]}')
