import copy

dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]

def dfs(i, direction, lst):
  global canOut
  blueOut = False
  if i == 10:
    return
  # print(lst)
  for d in dir:
    narr = copy.deepcopy(lst)
    # 이전 것과 똑같으면 굳이 안해도 되므로
    if direction != d:
      if d == [1, 0] or d == [0, 1]:
        for r in range(N - 1, -1, -1):
          for c in range(M - 1, -1, -1):
            # 벽에 닿을 때까지 움직이기
            if narr[r][c] == 'B' or narr[r][c] == 'R':
              word = ''
              if narr[r][c] == 'B':
                word = 'B'
              if narr[r][c] == 'R':
                word = 'R'
              a, b = r, c
              while True:
                a, b = a + d[0], b + d[1]
                # 벽에 닿으면 멈추기
                if narr[a][b] == '#':
                  break
                # 구멍에 도착하면 끝, 근데 파랑도 구멍에 도착하면 안됨표시
                if narr[a][b] == 'O':
                  if narr[a - d[0]][b - d[1]] == 'R':
                    narr[a - d[0]][b - d[1]] = '.'
                    canOut = True
                  if narr[a - d[0]][b - d[1]] == 'B':
                    blueOut = True
                  break
                # B이면 앞에 R이 있으면 멈춰라
                if word == 'B':
                  if narr[a][b] == 'R':
                    break
                # R이면 앞에 B이 있으면 멈춰라
                if word == 'R':
                  if narr[a][b] == 'B':
                    break
                # 다 아니면 갱신
                if word == 'B':
                  narr[a - d[0]][b - d[1]] = '.'
                  narr[a][b] = 'B'
                if word == 'R':
                  narr[a - d[0]][b - d[1]] = '.'
                  narr[a][b] = 'R'
            if blueOut == True:
              break
          if blueOut == True:
            break
        # 다 끝났으면
        if blueOut == True:
          canOut = False
          blueOut = False
          continue
        if canOut == True:
          print(1)
          exit()
        if lst != narr:
          dfs(i + 1, d, narr)
        
      if d == [0, -1] or d == [-1, 0]:
        for r in range(N):
          for c in range(M):
            # 벽에 닿을 때까지 움직이기
            if narr[r][c] == 'B' or narr[r][c] == 'R':
              word = ''
              if narr[r][c] == 'B':
                word = 'B'
              if narr[r][c] == 'R':
                word = 'R'
              a, b = r, c
              while True:
                a, b = a + d[0], b + d[1]
                # 벽에 닿으면 멈추기
                if narr[a][b] == '#':
                  break
                # 구멍에 도착하면 끝, 근데 파랑도 구멍에 도착하면 안됨표시
                if narr[a][b] == 'O':
                  if narr[a - d[0]][b - d[1]] == 'R':
                    narr[a - d[0]][b - d[1]] = '.'
                    canOut = True
                  if narr[a - d[0]][b - d[1]] == 'B':
                    blueOut = True
                  break
                # B이면 앞에 R이 있으면 멈춰라
                if word == 'B':
                  if narr[a][b] == 'R':
                    break
                # R이면 앞에 B이 있으면 멈춰라
                if word == 'R':
                  if narr[a][b] == 'B':
                    break
                # 다 아니면 갱신
                if word == 'B':
                  narr[a - d[0]][b - d[1]] = '.'
                  narr[a][b] = 'B'
                if word == 'R':
                  narr[a - d[0]][b - d[1]] = '.'
                  narr[a][b] = 'R'
            if blueOut == True:
              break
          if blueOut == True:
            break
        # 다 끝났으면
        if blueOut == True:
          canOut = False
          blueOut = False
          continue
        if canOut == True:
          print(1)
          exit()
        if lst != narr:
          dfs(i + 1, d, narr)
  

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

# 4방향으로 기울이는 dfs
canOut = False
dfs(0, 0, arr)
# 다 돌았어도 안되면
print(0)