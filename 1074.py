def findZ(N, r, c):
  if r == 0 and c == 0:
    return 0
  elif r == 0 and c == 1:
    return 1
  elif r == 1 and c == 0:
    return 2
  elif r == 1 and c == 1:
    return 3

  half = 2 ** (N - 1)
  num = half * half
  # 왼쪽 위에 있으면
  if r < half and c < half:
    return findZ(N - 1, r, c)
  # 오른쪽 위에 있으면
  elif r < half and c >= half:
    return num + findZ(N - 1, r, c - half)
  # 왼쪽 아래에 있으면
  elif r >= half and c < half:
    return num * 2 + findZ(N - 1, r - half, c)
  # 오른쪽 아래에 있으면
  else:
    return num * 3 + findZ(N - 1, r - half, c - half)

N, r, c = map(int, input().split())

cnt = findZ(N, r, c)
print(cnt)