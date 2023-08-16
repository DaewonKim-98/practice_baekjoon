def fibo(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        result = fibo(N - 1) + fibo(N - 2)
        return result
N = int(input())
print(fibo(N))