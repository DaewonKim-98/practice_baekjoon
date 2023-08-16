def pactorial(N):
    if N == 0:
        return 1
    if N == 1:
        return 1
    else:
        result = N * pactorial(N - 1)
        return result
N = int(input())
print(pactorial(N))