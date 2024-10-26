import sys
input = sys.stdin.readline

def findDynamite(i):
  cnt = 0
  for j in link[i]:
    if visited[j[0]] == 0:
      visited[j[0]] = 1
      cnt += min(j[1], findDynamite(j[0]))

  if cnt == 0:
    return 20000
  else:
    return cnt


T = int(input().strip())
for _ in range(T):
  N, M = map(int, input().strip().split())
  link = [[] for _ in range(N + 1)]
  for _ in range(M):
    a, b, d = map(int, input().strip().split())
    link[a].append((b, d))
    link[b].append((a, d))

  if N == 1:
    print(0)
    exit()
  
  # 연결된 것들의 합과 자신과의 최소
  visited = [0] * (N + 1)
  visited[1] = 1
  minCnt = findDynamite(1)
  print(minCnt)