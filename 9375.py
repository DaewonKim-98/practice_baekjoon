import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
  N = int(input().strip())
  dic = {}
  for _ in range(N):
    clothes, kind = map(str, input().strip().split())
    if kind in dic:
      dic[kind] += 1
    else:
      dic[kind] = 1
  cnt = 1
  for k in dic.keys():
    cnt *= dic[k] + 1
  # 마지막 알몸일 경우 빼주기
  cnt -= 1
  print(cnt)