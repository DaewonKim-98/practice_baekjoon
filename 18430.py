def getFibre(r, c, f):
  global maxFibre
  maxFibre = max(maxFibre, f)
  if c == M:
    r += 1
    c = 0
  if r == N:
    return

  if visited[r][c] == 0:
    for boomarang in boomarangs:
      loc = []
      for d in boomarang:
        nr, nc = r + d[0], c + d[1]
        if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
          loc.append((nr, nc))
        else:
          break
      # 부매랑을 만들 수 있으면
      else:
        # print(loc)
        nf = 0
        for l in loc:
          visited[l[0]][l[1]] = 1
          nf += arr[l[0]][l[1]]
        # 중심은 강도가 2배이므로 한번 더 더해주기
        nf += arr[loc[0][0]][loc[0][1]]
        getFibre(r, c + 1, f + nf)
        # 재귀 끝났으면 방문 풀어주기
        for l in loc:
          visited[l[0]][l[1]] = 0
  getFibre(r, c + 1, f)

N, M = map(int, input().strip().split())
arr = [list(map(int, input().strip().split())) for _ in range(N)]

# 부매랑
boomarangs = [[[0, 0], [0, 1], [1, 0]], [[0, 0], [0, 1], [-1, 0]], [[0, 0], [0, -1], [1, 0]], [[0, 0], [0, -1], [-1, 0]]]
maxFibre = 0
visited = [[0] * M for _ in range(N)]

# dfs로
getFibre(0, 0, 0)
print(maxFibre)