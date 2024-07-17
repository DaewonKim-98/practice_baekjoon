N, K= map(int, input().split())
arr = list(map(int, input().split()))
# 누적합
arrSum = arr.copy()
for i in range(1, N):
    arrSum[i] += arrSum[i - 1]
arrSum = [0] + arrSum

# 누적합에 따라 개수 dic에 저장
dic = {}
for i in range(N + 1):
  if arrSum[i] in dic:
    dic[arrSum[i]] += 1
  else:
    dic[arrSum[i]] = 1

cnt = 0
# K가 0이면 누적합끼리 걍 보면 되므로
if K == 0:
  for i in dic.keys():
    cnt += (dic[i] * (dic[i] - 1)) // 2

# 0 보다크면
elif K > 0:
  dicValue = sorted(list(dic.keys()))
  start = 0
  end = 0
  
  while start < len(dicValue) and end < len(dicValue):
      if start == end:
          end += 1
          continue
      if arrSum[end] - arrSum[start] == K:
          cnt += dic[dicValue[end]] * dic[dicValue[start]]
          end += 1
      elif arrSum[end] - arrSum[start] > K:
          start += 1
      else:
          end += 1
          
else:
  dicValue = sorted(list(dic.keys()), reverse=True)
  start = 0
  end = 0
  
  while start < len(dicValue) and end < len(dicValue):
      if start == end:
          end += 1
          continue
      if arrSum[end] - arrSum[start] == K:
          cnt += dic[dicValue[end]] * dic[dicValue[start]]
          end += 1
      elif arrSum[end] - arrSum[start] < K:
          start += 1
      else:
          end += 1

# 마지막엔 누적합이 K인 것 찾기
print(cnt)