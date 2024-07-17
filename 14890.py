def findRoad(i):
    global cnt
    # i열
    rTrue = True
    sameHeight = 1
    visited = [0] * N
    for r in range(1, N):
        # 같은 높이면 패쓰
        if arr[r - 1][i] == arr[r][i]:
            sameHeight += 1
            continue
        # 높이가 2 이상 차이나면 끝
        if abs(arr[r - 1][i] - arr[r][i]) > 1:
            sameHeight = 1
            rTrue = False
            break
        # 높이가 1 차이나고 지금까지 같은 높이가 L개 있으면 되는 것이므로
        if arr[r][i] - arr[r - 1][i] == 1:
            if sameHeight < L:
                rTrue = False
                break
            # 되면 방문 표시
            else:
                for j in range(r - 1, r - 1 - L, -1):
                    visited[j] = 1
        if abs(arr[r][i] - arr[r - 1][i]) == 1:
            sameHeight = 1
            
    sameHeight = 1
    for r in range(N - 2, -1, -1):
        # 같은 높이면 패쓰
        if arr[r + 1][i] == arr[r][i]:
            sameHeight += 1
            continue
        # 높이가 2 이상 차이나면 끝
        if abs(arr[r + 1][i] - arr[r][i]) > 1:
            sameHeight = 1
            rTrue = False
            break
        # 높이가 1 차이나고 지금까지 같은 높이가 L개 있으면 되는 것이므로
        if arr[r][i] - arr[r + 1][i] == 1:
            if sameHeight < L:
                rTrue = False
                break
            # 되는데 방문된 곳이면 겹치므로
            else:
                for j in range(r + 1, r + 1 + L):
                    if visited[j] == 1:
                        rTrue = False
                        break
        if abs(arr[r][i] - arr[r + 1][i]) == 1:
            sameHeight = 1
    if rTrue == True:
        cnt += 1
        
    # i행
    cTrue = True
    sameHeight = 1
    visited = [0] * N
    for c in range(1, N):
        # 같은 높이면 패쓰
        if arr[i][c - 1] == arr[i][c]:
            sameHeight += 1
            continue
        # 높이가 2 이상 차이나면 끝
        if abs(arr[i][c] - arr[i][c - 1]) > 1:
            sameHeight = 1
            cTrue = False
            break
        # 높이가 1 차이나고 지금까지 같은 높이가 L개 있으면 되는 것이므로
        if arr[i][c] - arr[i][c - 1] == 1:
            if sameHeight < L:
                cTrue = False
                break
            # 되면 방문 표시
            else:
                for j in range(c - 1, c - 1 - L, -1):
                    visited[j] = 1
        if abs(arr[i][c] - arr[i][c - 1]) == 1:
            sameHeight = 1
            
    sameHeight = 1
    for c in range(N - 2, -1, -1):
        # 같은 높이면 패쓰
        if arr[i][c] == arr[i][c + 1]:
            sameHeight += 1
            continue
        # 높이가 2 이상 차이나면 끝
        if abs(arr[i][c] - arr[i][c + 1]) > 1:
            sameHeight = 1
            cTrue = False
            break
        # 높이가 1 차이나고 지금까지 같은 높이가 L개 있으면 되는 것이므로
        if arr[i][c] - arr[i][c + 1] == 1:
            if sameHeight < L:
                cTrue = False
                break
            # 되는데 방문된 곳이면 겹치므로
            else:
                for j in range(c + 1, c + 1 + L):
                    if visited[j] == 1:
                        cTrue = False
                        break
        if abs(arr[i][c] - arr[i][c + 1]) == 1:
            sameHeight = 1
    if cTrue == True:
        cnt += 1
        
        
N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 하나씩 보면서 찾기
cnt = 0
for i in range(N):
    findRoad(i)
    
print(cnt)