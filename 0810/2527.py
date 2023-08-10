for i in range(4):    
    a, b, c, d, x, y, z, w = map(int, input().split())

    # 두 직사각형을 포함하는 촤표계를 만듦
    arr = []
    r_min = min(b, y)
    r_max = max(d, w)
    c_min = min(a, x)
    c_max = max(c, z)
    for r in range(r_min, r_max + 1):
        arr.append([0] * (c_max - c_min + 1))

    # 좌표계에 맞게 또 새롭게 좌표를 다시 배정(원 좌표에서 최솟값들을 빼주면 됨)
    a -= c_min
    b -= r_min
    c -= c_min
    d -= r_min
    x -= c_min
    y -= r_min
    z -= c_min
    w -= r_min

    # 새 좌표의 길이
    r_range = r_max - r_min + 1
    c_range = c_max - c_min + 1

    # 두 직사각형 좌표에 1 추가
    for i in range(b, d + 1):
        for j in range(a, c + 1):
            arr[i][j] += 1

    for i in range(y, w + 1):
        for j in range(x, z + 1):
            arr[i][j] += 1

    # 2가 없으면 안겹친다는 뜻이므로 d 출력
    lst = []
    for i in range(r_range):
        for j in range(c_range):
            lst.append(arr[i][j])

    if 2 not in lst:
        print('d')

    # 2가 하나 있으면 점이 겹치므로 c 출력
    elif arr.count(2) == 1:
        print('c')

    else:
        cnt = 0
        # 행 우선 탐색
        for r in range(r_range):
            # 각 행마다 2를 탐색한다.
            line = 0
            for c in range(c_range):
                if arr[r][c] == 2:
                    line += 1
            # 근데 만약 line이 1개라면 겹치는 부분이 열로 만들어져있다는 것이므로
            # line이 1 이상일 때 줄의 개수 cnt에 1을 추가해준다..
            if line > 1:
                cnt += 1

        # 열 우선 탐색
        for c in range(c_range):
            # 각 열마다 2를 탐색한다.
            line = 0
            for r in range(r_range):
                if arr[r][c] == 2:
                    line += 1
            # 근데 만약 line이 1개라면 겹치는 부분이 열로 만들어져있다는 것이므로
            # line이 1 이상일 때 줄의 개수 cnt에 1을 추가해준다...
            if line > 1:
                cnt += 1


        # cnt 가 1이라면 선분만 겹치는 것이므로
        if cnt == 1:
            print('b')
        else:
            print('a')