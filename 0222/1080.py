# 3*3 바꾸기
def change(r, c, arr):
  for i in range(3):
    for j in range(3):
      if arr[r + i][c + j] == 1:
        arr[r + i][c + j] = 0
      else:
        arr[r + i][c + j] = 1
  return arr

N, M = map(int, input().split())
A = [list(map(int, input())) for _ in range(N)]
B = [list(map(int, input())) for _ in range(N)]

# 아 그냥 같을 때 생각 안했네
if A == B:
  print(0)
  exit()
  
# 3*3 보다 작으면 안되므로
if len(A) < 3 or len(A[0]) < 3:
  print(-1)
  exit()

cnt = 0
# 전체를 돌면서 다른 부분이면 일단 바꿔 그냥
for r in range(N - 3 + 1):
  for c in range(M - 3 + 1):
    if A[r][c] != B[r][c]:
      A = change(r, c, A)
      cnt += 1
      
# 다 돌았을 때 같으면 끝
if A == B:
  print(cnt)
else:
  print(-1)
  