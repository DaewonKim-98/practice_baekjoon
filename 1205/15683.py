from copy import deepcopy

dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def dfs(arr, cnt, r, c):
    global max_cnt
    if r == N:
        max_cnt = max(cnt, max_cnt)
        return

    x, y = r, c
    # print(x, y)
    if arr[x][y] == 1:
        for d in dir:
            new_cnt = cnt
            new_arr = deepcopy(arr)
            nx, ny = x, y
            while 0 <= nx < N and 0 <= ny < M and new_arr[nx][ny] != 6:
                nx += d[0]
                ny += d[1]
                if 0 <= nx < N and 0 <= ny < M and new_arr[nx][ny] == 0:
                    new_arr[nx][ny] = '#'
                    new_cnt += 1
            if y == M - 1:
                new_x, new_y = x + 1, 0
            else:
                new_x, new_y = x, y + 1
            dfs(new_arr, new_cnt, new_x, new_y)
            
    elif arr[x][y] == 2:
        for d in [[0, 1], [1, 0]]:
            new_cnt = cnt
            new_arr = deepcopy(arr)
            nx, ny = x, y
            while 0 <= nx < N and 0 <= ny < M and new_arr[nx][ny] != 6:
                nx += d[0]
                ny += d[1]
                if 0 <= nx < N and 0 <= ny < M and  new_arr[nx][ny] == 0:
                    new_arr[nx][ny] = '#'
                    new_cnt += 1
            nx, ny = x, y 
            while 0 <= nx < N and 0 <= ny < M and new_arr[nx][ny] != 6:
                nx -= d[0]
                ny -= d[1]
                if 0 <= nx < N and 0 <= ny < M and  new_arr[nx][ny] == 0:
                    new_arr[nx][ny] = '#'
                    new_cnt += 1
            if y == M - 1:
                new_x, new_y = x + 1, 0
            else:
                new_x, new_y = x, y + 1
            dfs(new_arr, new_cnt, new_x, new_y)
            
    elif arr[x][y] == 3:
        for d in dir:
            new_cnt = cnt
            new_arr = deepcopy(arr)
            nx, ny = x, y
            while 0 <= nx < N and 0 <= ny < M and new_arr[nx][ny] != 6:
                nx += d[0]
                ny += d[1]
                if 0 <= nx < N and 0 <= ny < M and new_arr[nx][ny] == 0:
                    new_arr[nx][ny] = '#'
                    new_cnt += 1
            nx, ny = x, y
            while 0 <= nx < N and 0 <= ny < M and new_arr[nx][ny] != 6:
                nx += d[1]
                ny -= d[0]
                if 0 <= nx < N and 0 <= ny < M and new_arr[nx][ny] == 0:
                    new_arr[nx][ny] = '#'
                    new_cnt += 1
            if y == M - 1:
                new_x, new_y = x + 1, 0
            else:
                new_x, new_y = x, y + 1
            dfs(new_arr, new_cnt, new_x, new_y)

    elif arr[x][y] == 4:
        for d in dir:
            new_cnt = cnt
            new_arr = deepcopy(arr)
            nx, ny = x, y
            while 0 <= nx < N and 0 <= ny < M and new_arr[nx][ny] != 6:
                nx += d[0]
                ny += d[1]
                if 0 <= nx < N and 0 <= ny < M and new_arr[nx][ny] == 0:
                    new_arr[nx][ny] = '#'
                    new_cnt += 1
            nx, ny = x, y
            while 0 <= nx < N and 0 <= ny < M and new_arr[nx][ny] != 6:
                nx -= d[0]
                ny -= d[1]
                if 0 <= nx < N and 0 <= ny < M and new_arr[nx][ny] == 0:
                    new_arr[nx][ny] = '#'
                    new_cnt += 1
            nx, ny = x, y
            while 0 <= nx < N and 0 <= ny < M and new_arr[nx][ny] != 6:
                nx += d[1]
                ny -= d[0]
                if 0 <= nx < N and 0 <= ny < M and new_arr[nx][ny] == 0:
                    new_arr[nx][ny] = '#'
                    new_cnt += 1
            if y == M - 1:
                new_x, new_y = x + 1, 0
            else:
                new_x, new_y = x, y + 1
            dfs(new_arr, new_cnt, new_x, new_y)
    
    elif arr[x][y] == 5:
        new_cnt = cnt
        new_arr = deepcopy(arr)
        nx, ny = x, y
        while 0 <= nx < N and 0 <= ny < M and new_arr[nx][ny] != 6:
            nx += 1
            ny += 0
            if 0 <= nx < N and 0 <= ny < M and new_arr[nx][ny] == 0:
                new_arr[nx][ny] = '#'
                new_cnt += 1
        nx, ny = x, y
        while 0 <= nx < N and 0 <= ny < M and new_arr[nx][ny] != 6:
            nx += -1
            ny += 0
            if 0 <= nx < N and 0 <= ny < M and new_arr[nx][ny] == 0:
                new_arr[nx][ny] = '#'
                new_cnt += 1
        nx, ny = x, y
        while 0 <= nx < N and 0 <= ny < M and new_arr[nx][ny] != 6:
            nx += 0
            ny += 1
            if 0 <= nx < N and 0 <= ny < M and new_arr[nx][ny] == 0:
                new_arr[nx][ny] = '#'
                new_cnt += 1
        nx, ny = x, y
        while 0 <= nx < N and 0 <= ny < M and new_arr[nx][ny] != 6:
            nx += 0
            ny += -1
            if 0 <= nx < N and 0 <= ny < M and new_arr[nx][ny] == 0:
                new_arr[nx][ny] = '#'
                new_cnt += 1
        if y == M - 1:
            new_x, new_y = x + 1, 0
        else:
            new_x, new_y = x, y + 1
        dfs(new_arr, new_cnt, new_x, new_y)
        
    else:
        if y == M - 1:
            new_x, new_y = x + 1, 0
        else:
            new_x, new_y = x, y + 1
        dfs(arr, cnt, new_x, new_y)
        
        
            

            
            
        
    

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 사각지대가 최소이려면 최대한 많은 곳을 감시해야 하므로
# dfs를 통해 개수 찾기
# 일단 사각지대가 될 수 없는 것들 개수 세주기
max_cnt = 0
cnt = 0
for r in range(N):
    for c in range(M):
        if arr[r][c] != 0:
            cnt += 1
# print(cnt)          
dfs(arr, cnt, 0, 0)
# print(max_cnt)
print(N * M - max_cnt)