T = int(input())
for case in range(1 ,T + 1):
  n, d = map(int, input().split())
  arr = [list(map(int, input().split())) for _ in range(n)]
  
  # 시계방향 d만큼 돌리기
  if d > 0:
    for _ in range(d // 45):
      for i in range(n // 2):
        first = arr[i][i]
        arr[i][i] = arr[n // 2][i]
        arr[n // 2][i] = arr[n - 1 - i][i]
        arr[n - 1 - i][i] = arr[n - 1 - i][n // 2]
        arr[n - 1 - i][n // 2] = arr[n - 1 - i][n - 1 - i]
        arr[n - 1 - i][n - 1 - i] = arr[n // 2][n - 1 - i]
        arr[n // 2][n - 1 - i] = arr[i][n - 1 - i]
        arr[i][n - 1 - i] = arr[i][n // 2]
        arr[i][n // 2] = first
    
  # 시계반대방향
  else:
    for _ in range(-d // 45):
      for i in range(n // 2):
        first = arr[i][i]
        arr[i][i] = arr[i][n // 2]
        arr[i][n // 2] = arr[i][n - 1 - i]
        arr[i][n - 1 - i] = arr[n // 2][n - 1 - i]
        arr[n // 2][n - 1 - i] = arr[n - 1 - i][n - 1 - i]
        arr[n - 1 - i][n - 1 - i] = arr[n - 1 - i][n // 2]
        arr[n - 1 - i][n // 2] = arr[n - 1 - i][i]
        arr[n - 1 - i][i] = arr[n // 2][i]
        arr[n // 2][i] = first
        
  for r in range(n):
    for c in range(n):
      print(arr[r][c], end=' ')
    print()