import sys
input = sys.stdin.readline

def getTime(i):
  # 선수 과목이 없으면 1학기 이수
  if len(subjects[i]) == 0:
    visited[i] = 1
    time[i] = 1
    return 1
  
  # 이미 시간을 알았으면
  if time[i] > 0:
    return time[i]
  
  maxTime = 0
  visited[i] = 1
  for j in subjects[i]:
    maxTime = max(maxTime, getTime(j))
  
  time[i] = maxTime + 1
  return maxTime

N, M = map(int, input().strip().split())

subjects = [[] for i in range(N + 1)]
for _ in range(M):
  a, b = map(int, input().strip().split())
  subjects[b].append(a)
  
visited = [0] * (N + 1)
time = [0] * (N + 1)
for i in range(1, N + 1):
  getTime(i)

for i in range(1, N + 1):
  print(time[i], end=' ')