T = int(input())


for i in range(T):
    k = int(input())
    n = int(input())
    room = []
    # 0층을 먼저 만든다.
    for r in range(1, n + 1):
        room.append(r)
    # 각 층의 리스트를 만든다.
    floor = [room]
    # 1호는 무조건 1명
    if n == 1:
        print(1)
    # k 층에 대해 n호는 k 층의 n-1호 + k -1 층의 n호의 합과 같으므로
    else:
        for f in range(1, k + 1):
            n_room = [1]
            for r in range(1, n):
                n_room.append(n_room[r - 1] + floor[f - 1][r])
            floor.append(n_room)
        print(floor[k][n-1])
