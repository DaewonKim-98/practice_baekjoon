from itertools import permutations
from copy import deepcopy

# 회전 연산
def rotateArr(r, c, s):
  # s만큼 회전
  for i in range(1, s + 1):
    topLeft = arrCopy[r - i][c - i]
    topRight = arrCopy[r - i][c + i]
    bottomLeft = arrCopy[r + i][c - i]
    bottomRight = arrCopy[r + i][c + i]
    # 위
    for j in range(c + i, c - i, -1):
      arrCopy[r - i][j] = arrCopy[r - i][j - 1]
    # 오른쪽
    for j in range(r + i, r - i, -1):
      arrCopy[j][c + i] = arrCopy[j - 1][c + i]
    # 아래
    for j in range(c - i, c + i):
      arrCopy[r + i][j] = arrCopy[r + i][j + 1]
    # 왼쪽
    for j in range(r - i, r + i):
      arrCopy[j][c - i] = arrCopy[j + 1][c - i]
    # 갱신
    arrCopy[r - i][c - i + 1] = topLeft
    arrCopy[r - i + 1][c + i] = topRight
    arrCopy[r + i - 1][c - i] = bottomLeft
    arrCopy[r + i][c + i - 1] = bottomRight

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 회전 연산
rotateList = [tuple(map(int, input().split())) for _ in range(K)]

# 회전 연산의 순서의 경우의 수(순열)
allRotate = list(permutations(rotateList, K))

# 각 순열을 돌면서 최솟값 찾기
minValue = 100 * N * M
for rl in allRotate:
  arrCopy = deepcopy(arr)
  # 순열에서 회전연산들을 순서대로 돌면서 연산
  for rotate in rl:
    r, c, s = rotate
    r -= 1
    c -= 1
    rotateArr(r, c, s)
  # 모두 다 돌았으면 갱신
  for r in range(N):
    minValue = min(sum(arrCopy[r]), minValue)
  # print(arrCopy)
print(minValue)