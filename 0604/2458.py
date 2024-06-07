import sys
from collections import deque
input = sys.stdin.readline

def find(student):
  global students
  q = deque([])
  visited = [0] * (N + 1)
  q.append(student)
  visited[student] = 1
  
  while q:
    i = q.popleft()
    for j in small[i]:
      if visited[j] == 0:
        q.append(j)
        visited[j] = 1
        students += 1
  
  q.append(student)
  while q:
    i = q.popleft()
    for j in tall[i]:
      if visited[j] == 0:
        q.append(j)
        visited[j] = 1
        students += 1

N, M = map(int, input().strip().split())
small = [[] for _ in range(N + 1)]
tall = [[] for _ in range(N + 1)]

for _ in range(M):
  a, b = map(int, input().strip().split())
  small[b].append(a)
  tall[a].append(b)
  
# 찾기
cnt = 0
for i in range(1, N + 1):
  students = 0
  find(i)
  if students == N - 1:
    cnt += 1
    
print(cnt)