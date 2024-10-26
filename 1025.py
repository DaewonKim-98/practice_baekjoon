N, M = map(int, input().split())
arr = [list(map(str, input())) for _ in range(N)]

maxNum = -1
for r in range(N):
  for c in range(M):
    # 행과 열의 등차
    for i in range(N):
      for j in range(M):
        num = ''
        num2 = ''
        num3 = ''
        num4 = ''
        num += arr[r][c]
        num2 += arr[r][c]
        num3 += arr[r][c]
        num4 += arr[r][c]
        if int(num) ** (1/2) == int(int(num) ** (1/2)):
          maxNum = max(int(num), maxNum)
        # 행과 열의 등차가 0이면
        if i == 0 and j == 0:
          pass
        # 0이 아니면 등차 더해주기
        else:
          ni, nj = i, j
          while r + ni < N and c + nj < M:
            num += arr[r + ni][c + nj]
            ni += i
            nj += j
            if int(num) ** (1/2) == int(int(num) ** (1/2)):
              maxNum = max(int(num), maxNum)
          ni, nj = i, j
          while r - ni >= 0 and c - nj >= 0:
            num2 += arr[r - ni][c - nj]
            ni += i
            nj += j
            if int(num2) ** (1/2) == int(int(num2) ** (1/2)):
              maxNum = max(int(num2), maxNum)
          ni, nj = i, j
          while r + ni < N and c - nj >= 0:
            num3 += arr[r + ni][c - nj]
            ni += i
            nj += j
            if int(num3) ** (1/2) == int(int(num3) ** (1/2)):
              maxNum = max(int(num3), maxNum)
          ni, nj = i, j
          while r - ni >= 0 and c + nj < M:
            num4 += arr[r - ni][c + nj]
            ni += i
            nj += j
            if int(num4) ** (1/2) == int(int(num4) ** (1/2)):
              maxNum = max(int(num4), maxNum)

print(maxNum)