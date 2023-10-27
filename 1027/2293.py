N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# dp로 하는데 K를 만들 수 있는 경우의 수를 dp로 만들기
dp = [0] * (K + 1)
