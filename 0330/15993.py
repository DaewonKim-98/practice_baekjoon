T = int(input())

dpOdd = [0] * 100001
dpEven = [0] * 100001
dpOdd[1] = 1
dpOdd[2] = 1
dpEven[2] = 1
dpOdd[3] = 2
dpEven[3] = 2

# dp
for i in range(4, 100001):
    dpOdd[i] = (dpEven[i - 1] + dpEven[i - 2] + dpEven[i - 3]) % 1000000009
    dpEven[i] = (dpOdd[i - 1] + dpOdd[i - 2] + dpOdd[i - 3]) % 1000000009

for _ in range(T):
    N = int(input())
    print(dpOdd[N], dpEven[N])