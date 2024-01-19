import sys
input = sys.stdin.readline

N = int(input().strip())
arr = list(input().strip())

# 앞에서부터 떨어진 개수 세기(앞으로 옮기기)
color = arr[0]
color_cnt = 0
reverse_cnt = 0
i = 1
# 0번째와 똑같은 값이 오지 않을 때까지
while i < N and arr[i] == color:
  i += 1
while i < N:
  # 다른 색이면
  if arr[i] != color:
    reverse_cnt += 1
  # 같은 색이면
  else:
    color_cnt += 1
  i += 1
    
# 뒤에서부터 떨어진 개수 세기(앞으로 옮기기)
color = arr[N - 1]
color_cnt2 = 0
reverse_cnt2 = 0
i = N - 2
# 0번째와 똑같은 값이 오지 않을 때까지
while i >= 0 and arr[i] == color:
  i -= 1
while i >= 0:
  # 다른 색이면
  if arr[i] != color:
    reverse_cnt2 += 1
  # 같은 색이면
  else:
    color_cnt2 += 1
  i -= 1
    
# 최솟값 출력
print(min(color_cnt, color_cnt2, reverse_cnt, reverse_cnt2))