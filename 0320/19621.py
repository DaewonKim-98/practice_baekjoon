def dfs(i, num):
  global max_people
  if i == N - 1:
    if num > max_people:
      max_people = num
  
  min_next = 2 ** 31
  for j in range(i + 1, N):
    if arr[i][1] <= arr[j][0]:
      # if arr[j][1] < min_next:
      #   min_next = arr[j][1]
      dfs(j, num + arr[j][2])
    # 만약 끝까지 가도 if문에 들어가지 않는다면 강제로 넣기
    elif j == N - 1:
      dfs(j, num)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()

# dfs를 통해 가장 많은 회의 인원 찾기
max_people = 0
for i in range(N):
  dfs(i, arr[i][2])
  
print(max_people)