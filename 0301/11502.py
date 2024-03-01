from itertools import combinations_with_replacement

T = int(input())

# 소수 찾기
primes = []
for i in range(2, 1000):
    isPrime = True
    for j in range(2, int(i ** (1 / 2)) + 1):
        if i % j == 0:
            isPrime = False
            break
    if isPrime == True:
        primes.append(i)

# print(primes)
# 소수들을 3개로 묶기
primes3 = list(combinations_with_replacement(primes, 3))

for case in range(1, T + 1):
    K = int(input())
    # 3개로 묶은걸 돌면서 합이 K인거 찾기
    for p in primes3:
        if sum(p) == K:
            sorted_p = sorted(p)
            for i in sorted_p:
                print(i, end=' ')
            print()
            break
    # 없으면
    else:
        print(0)
