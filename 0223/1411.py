N = int(input())
arr = [list(input()) for _ in range(N)]

# 같은 쌍을 묶은 딕셔너리
dic = {}
# 전체를 돌면서 visited에 없으면 그것 탐색
visited = set()
for i in range(N - 1):
  if i not in visited:
    dic[i] = set()
    # 같은 문자들이 있는 인덱스들을 딕셔너리로
    same_word = {}
    for index in range(len(arr[i])):
      if arr[i][index] in same_word:
        same_word[arr[i][index]].append(index)
      else:
        same_word[arr[i][index]] = [index]
    # print(i, same_word)
    # 이후를 돌면서
    for j in range(i + 1, N):
      # i번째랑 비교해서 샴이면 dic, visited에 추가
      sham = True
      # 같은 문자들이 있는 인덱스들을 딕셔너리로
      jsame_word = {}
      for index in range(len(arr[j])):
        if arr[j][index] in jsame_word:
          jsame_word[arr[j][index]].append(index)
        else:
          jsame_word[arr[j][index]] = [index]
      # same_word와 jsame_word를 비교해서 같은 인덱스 리스트가 없으면 다르므로
      for v in same_word.values():
        if v not in jsame_word.values():
          sham = False
          break
      if sham == True:
        dic[i].add(i)
        dic[i].add(j)
        visited.add(j)

# print(dic)
# 전체 dic을 돌면서 쌍 찾기
cnt = 0
for k, v in dic.items():
  cnt += (len(v) * (len(v) - 1)) // 2
  
print(cnt)