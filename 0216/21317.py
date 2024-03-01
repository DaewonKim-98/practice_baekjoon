def dfs(index, bigJump, energy):
  global min_energy
  # 끝에 도달하면
  if index == N - 1:
    min_energy = min(min_energy, energy)
    return
  # 끝을 넘으면
  elif index > N - 1:
    return
  # 빅점프에 도달하면 빅점프
  elif index == bigJump:
    dfs(index + 3, bigJump, energy + K)
  # 아니면 재귀
  else:
    dfs(index + 1, bigJump, energy + arr[index][0])
    dfs(index + 2, bigJump, energy + arr[index][1])
  

N = int(input())
arr = [[0, 0] for _ in range(N - 1)]
for i in range(N - 1):
  a, b = map(int, input().split())
  arr[i][0] = a
  arr[i][1] = b
  
K = int(input())


# dfs를 통해
# 큰 점프를 하는 곳들을 정해두고 dfs
min_energy = 100000
for big in range(N - 2):
  dfs(0, big, 0)
# 빅점프를 안해도 되니까 빅점프를 그냥 패스하는거도 넣기
dfs(0, 20, 0)
  
print(min_energy)