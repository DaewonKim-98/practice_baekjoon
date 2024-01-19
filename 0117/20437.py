import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
  W = input().strip()
  K = int(input().strip())

  # 1 예외
  if K == 1:
    print(1, 1)
  
  else:
    max_length = 0
    min_length = 10001
    # 문자의 개수를 딕셔너리에 저장하고 각 문자들의 인덱스도 저장
    dic = {}
    for i in range(len(W)):
      # 딕셔너리에 없으면
      if W[i] not in dic:
        dic[W[i]] = [1, i]

      # 있으면
      else:
        # 개수 추가
        dic[W[i]][0] += 1
        # 인덱스 추가
        dic[W[i]].append(i)

        # 만약 개수가 K개 이상이 되면 그 사이의 길이를 구하고 짧은 문자열,
        # 긴 문자열 갱신
        if dic[W[i]][0] >= K:
          max_length = max(max_length, i - dic[W[i]][dic[W[i]][0] - K + 1])
          min_length = min(min_length, i - dic[W[i]][dic[W[i]][0] - K + 1])
          
    # 출력
    if max_length == 0:
      print(-1)
    else:
      print(min_length + 1, max_length + 1)