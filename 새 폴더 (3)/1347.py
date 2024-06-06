# 최대 길이가 50이라고 생각하면 101 * 101의 가운데에서 시작해서
# 움직이는 만큼 잘라버리기
import pprint

N = int(input())
move = list(input())
arr = [['#'] * 101 for _ in range(101)]

# 현재 위치는 50, 50
arr[50][50] = '.'
r, c = 50, 50
dirList = [[1, 0], [0, -1], [-1, 0], [0, 1]]
dir = 0

for m in move:
  if m == 'R':
    dir += 1
    dir %= 4
  elif m == 'L':
    dir += 4
    dir -= 1
    dir %= 4
  elif m == 'F':
    r, c = r + dirList[dir][0], c + dirList[dir][1]
    arr[r][c] = '.'
  
# 처음으로 .이 나온 시점부터 마지막이 .이 나온 시점까지가 미로 지도
firstR = 101
firstC = 101
lastR = 0
lastC = 0
for r in range(101):
  for c in range(101):
    if arr[r][c] == '.':
      firstR = min(firstR, r)
      firstC = min(firstC, c)
      lastR = max(lastR, r)
      lastC = max(lastC, c)
      
for r in range(firstR, lastR + 1):
  for c in range(firstC, lastC + 1):
    print(arr[r][c], end='')
  print()