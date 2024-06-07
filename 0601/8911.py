import sys

T = int(input().strip())
for _ in range(T):
  dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
  i = 0
  top = 0
  bottom = 0
  left = 0
  right = 0
  r = 0
  c = 0
  order = list(input().strip())

  # 거북이 움직인 영역의 최대, 최소 저장
  for j in order:
    if j == 'L':
      i += 4
      i -= 1
      i %= 4
    elif j == 'R':
      i += 1
      i %= 4
    elif j == 'F':
      r, c = r + dir[i][0], c + dir[i][1]
      top = max(r, top)
      bottom = min(r, bottom)
      left = min(c, left)
      right = max(c, right)
    else:
      r, c = r - dir[i][0], c - dir[i][1]
      top = max(r, top)
      bottom = min(r, bottom)
      left = min(c, left)
      right = max(c, right)
    # print(r, c)
  print(abs(top - bottom) * abs(right - left))