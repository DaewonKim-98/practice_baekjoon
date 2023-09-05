def tri(N):
    # 규칙대로 풀기
    tlist = [0] * 101
    tlist[1] = 1
    tlist[2] = 1
    tlist[3] = 1
    tlist[4] = 2
    tlist[5] = 2
    for i in range(6, N + 1):
        tlist[i] = tlist[i - 1] + tlist[i - 5]

    return tlist[N]

T = int(input())

for case in range(1, T + 1):
    N = int(input())
    print(tri(N))