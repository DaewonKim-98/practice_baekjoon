while True:
    N = int(input())
    if N == 0:
        break

    # 각 수들이 지워졌는지 아닌지를 나타내는 zlist / 0과 1 부분은 어차피 소수가 아니므로 0
    zlist = [0, 0] + [1] * (N * 2 - 1)
    # N 까지의 수에서 2부터 시작해서 각 수들의 배수들을 모두 지운다.
    for i in range(2, int((N * 2)** (1 / 2)) + 1):
        # zlist 에서 안지워진 부분이면 소수이므로
        if zlist[i] == 1:
            j = 2

            # i, 소수의 배수가 N 까지 갈때까지 지운다.
            while i * j <= 2 * N:
                zlist[i * j] = 0
                j += 1

    # 범위에서 1의 개수를 세면 소수의 개수
    print(zlist[N + 1:2 * N + 1].count(1))
