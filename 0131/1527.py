def dfs(i, num):
  global cnt
  # b의 개수에 도달했을 때
  if i == len(b):
    if int(a) <= int(num) <= int(b):
      cnt += 1
    return
  
  # a와 b 사이일 때
  if num and int(a) <= int(num) <= int(b):
    cnt += 1
    
  for j in ['4', '7']:
    dfs(i + 1, num + j)


a, b = map(str, input().split())

# 아 진짜 왜케 어렵냐 아옴ㄴ아ㅣ룸니;ㅏㅇㄻ낭럼니ㅏ

# dfs를 통해?
cnt = 0
dfs(0, '')
print(cnt)