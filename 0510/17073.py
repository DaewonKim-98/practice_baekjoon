import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(i):
  existChild = False
  child = 0
  for j in link[i]:
    if visited[j] == 0:
      child += 1
  for j in link[i]:
    # 자식한테 물 주기
    if visited[j] == 0:
      existChild = True
      arr[j] += arr[i] / child
      visited[j] = 1
      dfs(j)
  # 자식이 있으면 자기꺼 없앰
  if existChild == True:
    arr[i] = 0
  

N, W = map(int, input().strip().split())
link = [[] for _ in range(N + 1)]
for _ in range(N - 1):
  u, v = map(int, input().strip().split())
  link[u].append(v)
  link[v].append(u)

# 물의 양을 나타내는 arr
arr = [0] * (N + 1)
arr[1] = W

# 자식들한테 물 주기
visited = [0] * (N + 1)
visited[1] = 1
dfs(1)

# 물 있는 애들의 평균
cnt = 0
water = 0
# print(arr)
for i in range(N + 1):
  if arr[i] != 0:
    cnt += 1
    water += arr[i]
    
print(water / cnt)