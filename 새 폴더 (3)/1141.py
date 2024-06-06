N = int(input())
allSet = set()
for _ in range(N):
  allSet.add(input())

allSet = list(allSet)
# 길이가 긴 순서대로 정렬
allSet.sort(key=lambda x: len(x), reverse=True)
# 접두사가 안되는 것들 모두 넣기
notJubdu = set()
for word in allSet:
  isNotAllJubdu = True
  for j in notJubdu:
    isJubdu = True
    # 각 단어를 돌면서
    for i in range(min(len(word), len(j))):
      if word[i] != j[i]:
        isJubdu = False
        break
    # 하나라도 접두사가 되는게 있으면 안되므로
    if isJubdu == True:
      isNotAllJubdu = False
      break
  if isNotAllJubdu == True:
    notJubdu.add(word)
    
print(len(notJubdu))