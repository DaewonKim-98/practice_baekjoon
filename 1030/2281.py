N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# 정해진 순서대로 채워 넣으므로 dp 는 각 이름을 넣었을 때 최소의 제곱의 합
# 최대로 나올 수 있는 줄은 N줄이므로
dp = [0] * N
if sum(arr) + N - 1 <= M:
    print(0)
else:
    dp[0] = (M - arr[0]) ** 2
    for i in range(1, N):
        k = 1
        # i번째까지 이름을 적을 때 dp를 구하기
        for j in range(i + 1):
            if M * (k - 1) < arr[i:j]
            end = 0
