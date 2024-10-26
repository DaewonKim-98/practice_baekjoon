import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
P = int(input().strip())
K = int(input().strip())
# 최대 높이와 잘못 칠해진 칸의 열
maxHeight = 0
row = [0] * (M + 1)
for _ in range(K):
  a, b = map(int, input().strip().split())
  row[b] = 1
  maxHeight = max(maxHeight, a)

# 이분탐색일 것 같은데
start = maxHeight
end = M

while start <= end:
  mid = (start + end) // 2

  cnt = 0
  i = 1
  # 색종이로 가릴 수 있으면
  while i <= M:
    # 처음 가리는 곳이 나오면 다음 색종이로
    if row[i] == 1:
      i += mid
      cnt += 1
    # 안나오면 다음 찾기
    else:
      i += 1
  
  # 가릴 수 있는 색종이가 P개보다 적거나 같으면 색종이 크기 줄여도 되므로
  if cnt <= P:
    end = mid - 1
  # 아니면 색종이 크기를 늘려야 하므로
  else:
    start = mid + 1

print(start)