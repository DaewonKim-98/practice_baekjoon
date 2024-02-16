from collections import deque

def bfs(i):
  q = deque()
  q.append(i)
  visited[i] = 0

  while q:
    i = q.popleft()
    # 끝에 도달하면
    if i == N - 1:
      return visited[N - 1]
    
    for jump in range(1, arr[i] + 1):
      # 점프한 곳이 방문하지 않은 곳이면
      if i + jump < N and visited[i + jump] == 0:
        visited[i + jump] = visited[i] + 1
        q.append(i + jump)
        
  # 끝에 도달하지 못하면
  return -1
    
N = int(input())
arr = list(map(int, input().split()))

# bfs를 통해 찾기
visited = [0] * N
i = 0
print(bfs(i))