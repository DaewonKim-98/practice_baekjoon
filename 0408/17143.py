from copy import deepcopy

R, C, M = map(int, input().split())
arr = [[0] * C for _ in range(R)]

dir = [[-1, 0], [1, 0], [0, 1], [0, -1]]
# 상어 크기 dic
dic = {}

for _ in range(M):
  r, c, s, d, z = map(int, input().split())
  # 좌우면 속력은 C로 나눈 나머지
  if d == 3 or d == 4:
    s %= (C * 2 - 2)
  else:
    s %= (R * 2 - 2)
  dic[z] = [s, d - 1]
  arr[r - 1][c - 1] = z
# print(arr)
fish = 0
# 낚시왕 움직이면서 상어 잡기
for c in range(C):
  for r in range(R):
    # 상어 있으면 잡고 끝
    if arr[r][c] != 0:
      fish += arr[r][c]
      arr[r][c] = 0
      break
  narr = [[0] * C for _ in range(R)]
  # 상어 잡았으면 상어 움직이기
  for i in range(R):
    for j in range(C):
      if arr[i][j] != 0:
        # s만큼 움직이기
        s = dic[arr[i][j]][0]
        d = dic[arr[i][j]][1]
        ni, nj = i, j
        # print(i, j, arr[i][j], s, d)
        while s > 0:
          # 범위 안에 있으면 한칸씩
          if 0 <= ni + dir[d][0] < R and 0 <= nj + dir[d][1] < C:
            ni, nj = ni + dir[d][0], nj + dir[d][1]
            s -= 1
          # 범위 벗어나면 반대로 한칸
          else:
            if d == 0:
              d = 1
            elif d == 1:
              d = 0
            elif d == 2:
              d = 3
            else:
              d = 2
            dic[arr[i][j]][1] = d
            ni, nj = ni + dir[d][0], nj + dir[d][1]
            s -= 1
        # 움직인 위치로 상어 추가, 큰게 잡아먹기
        narr[ni][nj] = max(narr[ni][nj], arr[i][j])
  # 상어 다 옮겼으면 다시 arr 갱신
  arr = deepcopy(narr)
  # print(arr)
print(fish)
            
    