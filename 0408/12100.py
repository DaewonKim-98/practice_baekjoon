from copy import deepcopy

dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]

# 이동
def move(dir, arr):
  nnarr = deepcopy(arr)
  # 좌우
  if dir[0] == 0:
    # 좌로 움직이기
    if dir[1] == -1:
      for r in range(N):
        index = 0
        value = nnarr[r][0]
        for c in range(1, N):
          if nnarr[r][c] != 0:
            # print(nnarr, c)
            # 현재와 이전 것이 같으면 합칠 수 있으므로
            if nnarr[r][c] == value:
              nnarr[r][index] = value * 2
              nnarr[r][c] = 0
              index = c
              value = 0
            # 다르면
            else:
              value = nnarr[r][c]
              index = c
        # 모두 좌로 넣기
        index = 0
        for c in range(N):
          if nnarr[r][c] == 0:
            index = c
            break
        for c in range(index + 1, N):
          if nnarr[r][c] != 0 and nnarr[r][index] == 0:
            nnarr[r][index] = nnarr[r][c]
            nnarr[r][c] = 0
            index += 1
                  
    # 우로 움직이기
    else:
      for r in range(N):
        index = N - 1
        value = nnarr[r][N - 1]
        for c in range(N - 2, -1, -1):
          if nnarr[r][c] != 0:
            # 앞에와 똑같으면
            if value == nnarr[r][c]:
              nnarr[r][index] = 2 * value
              nnarr[r][c] = 0
              value = 0
            else:
              value = nnarr[r][c]
              index = c
        # 모두 우로 넣기
        index = N - 1
        for c in range(N - 1, -1, -1):
          if nnarr[r][c] == 0:
            index = c
            break
        for c in range(index - 1, -1, -1):
          if nnarr[r][c] != 0 and nnarr[r][index] == 0:
            nnarr[r][index] = nnarr[r][c]
            nnarr[r][c] = 0
            index -= 1
  # 상하
  if dir[1] == 0:
    # 위로 움직이기
    if dir[0] == -1:
      for c in range(N):
        index = 0
        value = nnarr[0][c]
        for r in range(1, N):
          if nnarr[r][c] != 0:
            # 앞에와 똑같으면
            if value == nnarr[r][c]:
              nnarr[index][c] = 2 * value
              nnarr[r][c] = 0
              value = 0
            else:
              value = nnarr[r][c]
              index = r
        # 모두 위로 넣기
        index = 0
        for r in range(N):
          if nnarr[r][c] == 0:
            index = r
            break
        for r in range(index + 1, N):
          if nnarr[r][c] != 0 and nnarr[index][c] == 0:
            nnarr[index][c] = nnarr[r][c]
            nnarr[r][c] = 0
            index += 1
            
    # 아래로 움직이기
    else:
      for c in range(N):
        index = N - 1
        value = nnarr[N - 1][c]
        for r in range(N - 2, -1, -1):
          if nnarr[r][c] != 0:
            # 앞에와 똑같으면
            if value == nnarr[r][c]:
              nnarr[index][c] = 2 * value
              nnarr[r][c] = 0
              value = 0
            else:
              value = nnarr[r][c]
              index = r
        # 모두 아래로 넣기
        index = N - 1
        for r in range(N - 1, -1, -1):
          if nnarr[r][c] == 0:
            index = r
            break
        for r in range(index - 1, -1, -1):
          if nnarr[r][c] != 0 and nnarr[index][c] == 0:
            nnarr[index][c] = nnarr[r][c]
            nnarr[r][c] = 0
            index -= 1
  # print(1, nnarr)
  return nnarr

# dfs
def dfs(i, arr):
  narr = deepcopy(arr)
  global maxBlock
  # 5번되면
  if i == 5:
    # print(arr)
    for r in range(N):
      # print(arr[r])
      maxBlock = max(maxBlock, max(arr[r]))
    return
  
  for d in dir:
    dfs(i + 1, move(d, narr))
    

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# dfs를 통해
maxBlock = 0
dfs(0, arr)
print(maxBlock)