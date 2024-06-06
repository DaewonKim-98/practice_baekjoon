import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(i):
  global parentSet
  if i in parentSet:
    print(i)
    return
  # 자식에서 부모로 계속 올라가기
  for j in link[i]:
    dfs(j)
    parentSet.add(j)

T = int(input().strip())
for case in range(1, T + 1):
  N = int(input().strip())
  link = [[] for _ in range(N + 1)]
  for _ in range(N - 1):
    a, b = map(int, input().strip().split())
    # 자식에서 부모를 저장
    link[b].append(a)
    
  a, b = map(int, input().strip().split())
  # dfs를 통해 부모로 쭉 올라가기
  parentSet = set()
  dfs(a)
  parentSet.add(a)
  dfs(b)