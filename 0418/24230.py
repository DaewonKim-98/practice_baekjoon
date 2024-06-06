import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(i, color):
  global cnt
  for j in link[i]:
    # 방문 안했으면 자식 노드이므로
    if visited[j] == 0:
      # 색이 바뀌면 색칠한 것이므로
      if arr[j] != color:
        cnt += 1
        colors.add(arr[j])
        visited[j] = 1
        dfs(j, arr[j])
      else:
        visited[j] = 1
        dfs(j, color)

N = int(input().strip())
arr =[0] + list(map(int, input().strip().split()))
link = [[] for _ in range(N + 1)]

for _ in range(N - 1):
  a, b = map(int, input().strip().split())
  link[a].append(b)
  link[b].append(a)

# 색칠한 것들에서 시작해서 다른 색이 나오면 새로 색칠하는 것이므로
visited = [0] * (N + 1)
cnt = 0
colors = set()
# 1부터 시작
visited[1] = 1
if arr[1] != 0:
  cnt += 1
dfs(1, arr[1])
print(cnt)