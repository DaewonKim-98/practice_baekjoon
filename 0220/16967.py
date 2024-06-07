H, W, X, Y = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(H + X)]


A = [[0] * W for _ in range(H)]

# B를 돌면서 두 배열 중 하나에 포함되는 부분을 A에 넣기
for i in range(H + X):
  for j in range(W + Y):
    if (0 <= i < X and 0 <= j < W) or (0 <= j < Y and 0 <= i < H):
      A[i][j] = B[i][j]
      
# 이제는 겹치는 부분 넣기
for i in range(H + X):
  for j in range(W + Y):
    if X <= i < H and Y <= j < W:
      A[i][j] = B[i][j] - A[i - X][j - Y]
      
for i in range(H):
  for j in range(W):
    print(A[i][j], end=' ')
  print()
  
  