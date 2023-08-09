T = int(input())

# 각 수들이 지워졌는지 아닌지를 나타내는 zlist / 0과 1 부분은 어차피 소수가 아니므로 0
zlist = [0, 0] + [1] * (1000000 - 1)
# N 까지의 수에서 2부터 시작해서 각 수들의 배수들을 모두 지운다.
for i in range(2, int(1000000 ** (1 / 2)) + 1):
    # zlist 에서 안지워진 부분이면 소수이므로
    if zlist[i] == 1:
        j = 2

        # i, 소수의 배수가 N 까지 갈때까지 지운다.
        while i * j <= 1000000:
            zlist[i * j] = 0
            j += 1

for case in range(1, T + 1):
    N = int(input())

    cnt = 0
    # 범위에서 1인 부분을 찾으면 소수인데 만약 소수면서 N에서 뺀 값도 소수면
    # 두 소수의 합이 N 이라는 것이므로
    for k in range(0, N // 2 + 1):
        if zlist[k] == 1 and zlist[N - k] == 1:
            cnt += 1

    print(cnt)
