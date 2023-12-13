from copy import deepcopy

N, M, K = map(int, input().split())
arr = [[0] * N for _ in range(N)]
dir = {
    0: [-1, 0],
    1: [-1, 1],
    2: [0, 1],
    3: [1, 1],
    4: [1, 0],
    5: [1, -1],
    6: [0, -1],
    7: [-1, -1]
}

# 파이어볼
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    arr[r - 1][c - 1] = [m, [s, 1], [d]]
    
# 파이어볼 이동
for i in range(K):
    arr_copy = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if arr[r][c] != 0:
                for j in arr[r][c][2]:
                    nr, nc = r + dir[j][0] * arr[r][c][1][0], c + dir[j][1] * arr[r][c][1][0]
                    if nr < 0:
                        if abs(nr) % N == 0:
                            nr = 0
                        else:
                            nr = N - (abs(nr) % N)
                    elif nr >= 0:
                        if nr % N == 0:
                            nr = 0
                        else:
                            nr = nr % N
                    if nc < 0:
                        if abs(nc) % N == 0:
                            nc = 0
                        else:
                            nc = N - (abs(nc) % N)
                    elif nc >= 0:
                        if nc % N == 0:
                            nc = 0
                        else:
                            nc = nc % N
                            
                    if arr_copy[nr][nc] == 0:
                        arr_copy[nr][nc] = [arr[r][c][0], [arr[r][c][1][0], 1], [j]]
                    else:
                        arr_copy[nr][nc][0] = arr[r][c][0] + arr_copy[nr][nc][0]
                        arr_copy[nr][nc][1] = [arr[r][c][1][0] + arr_copy[nr][nc][1][0], arr_copy[nr][nc][1][1] + 1]
                        arr_copy[nr][nc][2] = arr_copy[nr][nc][2] + [j]
                        
    # 파이어볼을 다 이동했으면 재정의
    # print(arr_copy)
    arr = arr_copy
    for r in range(N):
        for c in range(N):
            if arr[r][c] != 0:
                # 질량
                if arr[r][c][1][1] != 1:
                    arr[r][c][0] = arr[r][c][0] // 5
                # 질량이 0이면
                if arr[r][c][0] == 0:
                    arr[r][c] = 0
                    continue
                
                # 속력
                arr[r][c][1][0] = arr[r][c][1][0] // arr[r][c][1][1]
                
                # 방향
                if arr[r][c][1][1] != 1:
                    odd = False
                    even = False
                    for j in arr[r][c][2]:
                        if j % 2 == 1:
                            odd = True
                        else:
                            even = True
                    # 둘 다 True면 방향은 1 3 5 7
                    if odd == True and even == True:
                        arr[r][c][2] = [1, 3, 5, 7]
                    else:
                        arr[r][c][2] = [0, 2, 4, 6]
            
# 파이어볼 질량 합
mass = 0
for r in range(N):
    for c in range(N):
        if arr[r][c] != 0:
            if arr[r][c][1][1] != 1:
                mass += arr[r][c][0] * 4
            else:
                mass += arr[r][c][0]
            
print(mass)