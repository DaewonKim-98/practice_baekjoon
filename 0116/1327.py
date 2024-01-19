from collections import deque

def bfs(i):
  q = deque()
  q.append((i, 0))
  
  while q:
    lst, cnt = q.popleft()
    # 오름차순과 똑같으면
    if lst == copy_arr:
      return cnt
    # 뒤집을 수 있는 인덱스만큼 돌면서
    for j in range(N - K + 1):
      copy_lst = lst.copy()
      # 뒤집기
      for k in range(K // 2):
        copy_lst[j + k], copy_lst[j + K - k - 1] = copy_lst[j + K - k - 1], copy_lst[j + k]
      # 뒤집은게 방문하지 않은 곳이면
      if tuple(copy_lst) not in visited:
        q.append((copy_lst, cnt + 1))
        visited.add(tuple(copy_lst))
        
  # 모두를 다 돌았어도 오름차순이 없으면
  return -1

N, K = map(int, input().split())
arr = list(map(int, input().split()))

# 오름차순
copy_arr = arr.copy()
copy_arr.sort()

# 방문한 수열
visited = set(tuple(arr))
# bfs를 통해 모든 경우 탐색
print(bfs(arr))