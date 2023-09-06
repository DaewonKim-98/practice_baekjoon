import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

# O로 갈 때와 O를 지나고 갈 때를 나누면 조합으로 생각할 수 있는데
# (갈 수 있는 가로 + 세로)! / ((가로)! * (세로)!) 이므로 O가 어느 위치에 있는지 찾기만 하면 된다.

# N이나 M이 1이면 이동 경로는 무조건 1
if N == 1 or M == 1:
    print(1)

# K가 0이면 없다는 것이므로 끝까지 가면 됨
elif K == 0:
    r = N - 1
    c = M - 1

    s_pac = 1
    for i in range(1, r + c + 1):
        s_pac *= i
    r_pac = 1
    for j in range(1, r + 1):
        r_pac *= j
    c_pac = 1
    for k in range(1, c + 1):
        c_pac *= k

    go = s_pac // (r_pac * c_pac)
    print(go)

else:
    if K % M != 0:
        r = K // M
        c = K % M - 1
    else:
        r = K // M - 1
        c = M - 1

    # O로 갈 때
    s_pac = 1
    for i in range(1, r + c + 1):
        s_pac *= i
    r_pac = 1
    for j in range(1, r + 1):
        r_pac *= j
    c_pac = 1
    for k in range(1, c + 1):
        c_pac *= k

    go_o = s_pac // (r_pac * c_pac)

    # O에서 출발할 때
    r2 = N - r - 1
    c2 = M - c - 1

    s_pac = 1
    for i in range(1, r2 + c2 + 1):
        s_pac *= i
    r_pac = 1
    for j in range(1, r2 + 1):
        r_pac *= j
    c_pac = 1
    for k in range(1, c2 + 1):
        c_pac *= k

    from_o = s_pac // (r_pac * c_pac)

    # 결과는 두 경로의 수를 곱한 것
    print(go_o * from_o)