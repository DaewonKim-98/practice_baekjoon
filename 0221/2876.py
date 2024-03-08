N = int(input())

# 각 번호의 인덱스들 딕셔너리
dic = {
  1: set(),
  2: set(),
  3: set(),
  4: set(),
  5: set(),
}

# 돌면서 인덱스들 추가
for i in range(N):
  a, b = map(int, input().split())
  dic[a].add(i)
  dic[b].add(i)

# 이제 각 번호에서 최장 길이 찾기
max_length = 0
grade = 0

for k, v in dic.items():
  # 번호를 돌면서 연속되는 인덱스면 채점할 수 있으므로
  if v:
    v = list(v)
    v.sort()
    length = 1
    mlength = 1
    for i in range(1, len(v)):
      if v[i] == v[i - 1] + 1:
        length += 1
      # 연속되지 않으면 끝, 초기화
      else:
        mlength = max(mlength, length)
        length = 1
    mlength = max(mlength, length) 
      
    # 갱신
    if max_length < mlength:
      max_length = mlength
      grade = k
    
print(max_length, grade)