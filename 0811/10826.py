def fibonacci(N):
    fibo = [0] * 10000000
    fibo[0] = 0
    fibo[1] = 1
    fibo[2] = 1
    for i in range(2, N + 1):
        fibo[i] = fibo[i - 1] + fibo[i - 2]
    return fibo[N]

N = int(input())
print(fibonacci(N))