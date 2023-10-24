T = int(input())
for case in range(1, T + 1):
    N, E = map(int, input().split())
    arr = list(map(int, input().split()))
    E = E // 2

    # 세트와 용량을 나타내는 dp를 만들기
    dp = [[0, 0] * N for _ in range(N + 1)]
    