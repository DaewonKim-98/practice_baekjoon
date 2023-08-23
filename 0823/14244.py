import sys
input = sys.stdin.readline

N, M = map(int, input().split())

if M == 2:
    for i in range(N - 1):
        print(f'{i} {i + 1}')

else:
    for i in range(N - M + 1):
        print(f'{i} {i + 1}')
    for j in range(2, M):
        print(f'{N - M} {N - M + j}')