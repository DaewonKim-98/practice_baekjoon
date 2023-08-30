import sys
input = sys.stdin.readline

T = int(input().strip())
for case in range(1, T + 1):
    N, M = map(int, input().split())
    # 조합 계산
    c = 1
    for i in range(M, M - N, -1):
        c *= i
    for j in range(1, N + 1):
        c //= j

    print(c)