def game(r, c):
  global cnt
  if c == M:
    r += 1
    c = 0
  if r == N:
    cnt += 1
    return
  # 넴모 안올리고 한칸 이동
  arr[r][c] = 0
  game(r, c + 1)
  # 넴모 올리기
  arr[r][c] = 1
  # 넴모 4개가 되어 있으면 무효
  if r - 1 >= 0 and c - 1 >= 0:
    if arr[r][c] == arr[r][c - 1] == arr[r - 1][c] == arr[r - 1][c - 1] == 1:
      return
  game(r, c + 1)


N, M = map(int, input().split())
arr = [[0] * M for _ in range(N)]

# 넴모를 하나씩 올리면서
cnt = 0
game(0, 0)
print(cnt)