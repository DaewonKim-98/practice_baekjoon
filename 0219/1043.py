def bfs(j):
  q = []
  q.append(j)
  
  while q:
    j = q.pop(0)
    for k in range(M):
      # 방문하지 않고 j가 파티에 있으면 그 사람들도 연결되어 있는 것이므로
      if visited[k] == 0 and j in parties[k]:
        visited[k] = 1
        for l in parties[k]:
          if j != l:
            q.append(l)
            truth.add(l)

N, M = map(int, input().split())
truth = set(list(map(int, input().split()))[1:])
parties = []
for _ in range(M):
  lst = list(map(int, input().split()))
  parties.append(set(lst[1:]))

# 진실을 아는 사람들을 먼저 다 추가한 뒤 나머지 진실을 모르는 사람들만 있는
# 파티의 수가 최대로 갈 수 있는 파티의 수네 멍청한놈아
visited = [0] * M
for i in range(M):
  if visited[i] == 0:
    know_truth = False
    for j in parties[i]:
      if j in truth:
        know_truth = True
        break
    # 진실을 아는 사람이 한 명이라도 있으면 그 파티는 망한거
    if know_truth == True:
      visited[i] = 1
      # bfs를 통해 진실을 아는 사람과 연결된 모든 파티를 찾기
      for j in parties[i]:
        truth.add(j)
        bfs(j)
    
# 이제 진실을 알게 되는 모든 사람들이 다 나왔으므로 다시 파티를 돌면서
# 이 사람들이 없는 완벽한 파티를 즐길 수 있는지 찾으면 될듯
cnt = 0
for i in range(M):
  know_truth = False
  for j in parties[i]:
    if j in truth:
      know_truth = True
      break
  # 진실을 아는 사람이 없는 파티 세기
  if know_truth == False:
    cnt += 1
    
print(cnt)
  