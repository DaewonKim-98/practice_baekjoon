from collections import deque

dir = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ground = [[5] * N for _ in range(N)]
trees = [[deque() for _ in range(N)] for _ in range(N)]

for _ in range(M):
  x, y, z = map(int, input().split())
  trees[x - 1][y - 1].append(z)

# K년 동안 반복
for _ in range(K):
  for r in range(N):
    for c in range(N):
      cnt = 0
      # 양분 먹이거나 죽이거나
      treesCnt = len(trees[r][c])
      for _ in range(treesCnt):
        tree = trees[r][c].popleft()
        if tree <= ground[r][c]:
          ground[r][c] -= tree
          trees[r][c].append(tree + 1)
        else:
          cnt += tree // 2
      # 여름 양분 추가
      ground[r][c] += cnt
  # 가을 나무 번식
  for r in range(N):
    for c in range(N):
      for tree in trees[r][c]:
        if tree % 5 == 0:
          for d in dir:
            nr, nc = r + d[0], c + d[1]
            if 0 <= nr < N and 0 <= nc < N:
              trees[nr][nc].appendleft(1)
      # 겨울 양분 추가
      ground[r][c] += arr[r][c]

# 살아남은 나무의 수
cnt = 0
for r in range(N):
  for c in range(N):
    cnt += len(trees[r][c])

print(cnt)