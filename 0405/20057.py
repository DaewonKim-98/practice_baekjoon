from math import floor
import pprint

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 토네이도 방향
dir = [[0, -1], [1, 0], [0, 1], [-1, 0]]
# 흩날리는 방향
def scatterDir(direction):
  if direction[0] == 0:
    return [[-1, direction[1] * -1, 0.01],
            [1, direction[1] * -1, 0.01],
            [-1, 0, 0.07],
            [1, 0, 0.07],
            [-1, direction[1], 0.1],
            [1, direction[1], 0.1],
            [-2, 0, 0.02],
            [2, 0, 0.02],
            [0, direction[1] * 2, 0.05],
            ]
  else:
    return [[direction[0] * -1, -1, 0.01],
            [direction[0] * -1, 1, 0.01],
            [0, -1, 0.07],
            [0, 1, 0.07],
            [direction[0], -1, 0.1],
            [direction[0], 1, 0.1],
            [0, -2, 0.02],
            [0, 2, 0.02],
            [direction[0] * 2, 0, 0.05],
            ]


# 토네이도의 이동칸은 1, 1, 2, 2, 3, 3, ...
moveaAmount = []
for i in range(1, N):
  moveaAmount.append(i)
  moveaAmount.append(i)
# 마지막 하나 추가
moveaAmount.append(N - 1)

# 이동
move = []
for i in range(len(moveaAmount)):
  for j in range(moveaAmount[i]):
    move.append(i)
# 격자 밖으로 나간 모래
result = 0

# 토네이도 이동하면서 모래 흩날리기
r, c = N // 2, N // 2
for i in move:
  direction = dir[i % 4]
  # y의 모래를 흩날리므로
  yr, yc = r + direction[0], c + direction[1]
  # 모래양
  sand = arr[yr][yc]
  
  # 흩날리는 방향으로 모래 흩날리기
  # 알파를 구하기 위해 알파 제외하고 모으기
  notAlpha = 0
  # print(r, c)
  # print(result)
  # print(scatterDir(direction))
  for d in scatterDir(direction):
    nr, nc = yr + d[0], yc + d[1]
    # 격자 안이라면
    if 0 <= nr < N and 0 <= nc < N:
      arr[nr][nc] += floor(sand * d[2])
      notAlpha += floor(sand * d[2])
    # 격자 밖이라면
    else:
      result += floor(sand * d[2])
      notAlpha += floor(sand * d[2])
      
  # 다 흩날렸으면 알파로 나머지 보내기
  # 격자 밖으로 안나가면
  if 0 <= yr + direction[0] < N and 0 <= yc + direction[1] < N:
    arr[yr + direction[0]][yc + direction[1]] += sand - notAlpha
  else:
    result += sand - notAlpha
  arr[yr][yc] = 0
  r, c = yr, yc
#   pprint.pprint(arr)
# print(arr)   
print(result)