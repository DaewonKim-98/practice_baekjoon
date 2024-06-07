import sys
input = sys.stdin.readline

N = int(input().strip())
arr = []
for _ in range(N):
  arr.append(int(input().strip()))
  
check = []
# 볼 수 있는 아파트면 check에 추가, 못보면 빼기
i = 0
cnt = 0
while i < N:
  # 없으면 채우기
  if len(check) == 0:
    check.append(arr[i])
    i += 1
  # 볼 수 있으면
  elif arr[i] < check[-1]:
    cnt += len(check)
    check.append(arr[i])
    i += 1
  # 볼 수 없으면
  else:
    check.pop()
  # print(check, cnt)
    
print(cnt)