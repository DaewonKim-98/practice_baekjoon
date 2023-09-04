# import sys
# input = sys.stdin.readline

# N = int(input().strip())
# arr = [list(input().strip()) for _ in range(N)]

# # 가로로 돌면서 친구가 있으면 그 친구의 줄로 다시 가서 친구의 수 세기
# max_cnt = 0
# for r in range(N):
#     cnt = 0
#     c_list = []
#     for c in range(N):
#         if arr[r][c] == 'Y':
#             # 친구가 중복하는 경우는 빼주어야 하므로 친구 리스트 생성
#             c_list.append(c)
#             # 친구들의 친구들을 찾으면 결국 2- 친구
#             for c2 in range(N):
#                 if arr[c][c2] == 'Y':
#                     cnt += 1

#             # 친구 리스트에서 서로 친구인 경우는 중복이므로 제거
#             for r2 in c_list:
#                 for c3 in c_list:
#                     if arr[r2][c3] == arr[c3][r2] == 'Y':
#                         cnt -= 1
          
#     if max_cnt < cnt:
#         max_cnt = cnt

# print(max_cnt)


import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [list(sys.stdin.readline().strip()) for _ in range(n)]
# 2-친구 사이일 때 1, 아니면 0
f = [[0] * n for _ in range(n)]

for k in range(n):
  for i in range(n):
    for j in range(n):
      if i != j:
        # 2-친구인 경우 i, j가 친구이고 또 두명 다 친구인 k가 존재하면 되므로
        if graph[i][j] == 'Y' or (graph[i][k] == 'Y' and graph[k][j] =='Y'):
            f[i][j] = 1

ressult = 0

for row in f:
  result = max(ressult,sum(row))
print(result)
    