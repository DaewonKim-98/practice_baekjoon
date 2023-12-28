from copy import deepcopy

R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

for _ in range(T):
    # 미세먼지 확산
    dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    arr_copy = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            # 미세먼지가 있으면
            if arr[r][c] > 0:
                cnt = 0
                for d in dir:
                    nr, nc = r + d[0], c + d[1]
                    if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] != -1:
                        arr_copy[nr][nc] += arr[r][c] // 5
                        cnt += 1
                # 자기 자신도 줄이기
                arr_copy[r][c] += arr[r][c] - (arr[r][c] // 5) * cnt
            # 공기청정기
            elif arr[r][c] == -1:
                arr_copy[r][c] = -1
            
    arr = deepcopy(arr_copy)

    
    # 미세먼지 정화
    cnt = 0
    for r in range(R):
        # 위 공기청정기
        if arr[r][0] == -1 and cnt == 0:
            # 아래로 밀기
            for nr in range(r - 1, 0, -1):
                arr[nr][0] = arr[nr - 1][0]
            # 왼쪽으로 밀기
            for c in range(C - 1):
                arr[0][c] = arr[0][c + 1]
            # 위로 밀기
            for nr in range(1, r + 1):
               arr[nr - 1][C - 1] = arr[nr][C - 1]
            # 오른쪽으로 밀기
            for c in range(C - 2, 0, -1):
                arr[r][c + 1] = arr[r][c]
            arr[r][1] = 0
            cnt += 1
                      
        # 아래 공기청정기
        elif arr[r][0] == -1 and cnt == 1:
            # 위로 밀기
            for nr in range(r + 1, R - 1):
                arr[nr][0] = arr[nr + 1][0]
            # 왼쪽으로 밀기
            for c in range(C - 1):
                arr[R - 1][c] = arr[R - 1][c + 1]
            # 아래로 밀기
            for nr in range(R - 1, r, -1):
                arr[nr][C - 1] = arr[nr - 1][C - 1]
            # 오른쪽으로 밀기
            for c in range(C - 2, 0, -1):
                arr[r][c + 1] = arr[r][c]
            arr[r][1] = 0
    # print(arr)
    
# 미세먼지 양
cnt = 0
for r in range(R):
    for c in range(C):
        if arr[r][c] > 0:
            cnt += arr[r][c]
            
print(cnt)