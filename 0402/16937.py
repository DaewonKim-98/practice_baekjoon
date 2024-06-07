from itertools import combinations

H, W = map(int, input().split())
N = int(input())
sticker = []
for _ in range(N):
  r, c = map(int, input().split())
  sticker.append([r, c])
  
# 2개 정하기
stickers = list(combinations(sticker, 2))  
maxArea = 0
for s in stickers:
  # print(s[0][0], s[0][1], s[1][0],  s[1][1])
  # 가로로 2개 붙이는 경우
  # 세로 길이가 일단 H보다 작아야 하므로
  if s[0][0] <= H and s[1][0] <= H:
    if s[0][1] + s[1][1] <= W:
      maxArea = max(maxArea, s[0][0] * s[0][1] + s[1][0] * s[1][1])
  # 90도 돌렸을 때
  if s[0][0] <= H and s[1][1] <= H:
    if s[0][1] + s[1][0] <= W:
      maxArea = max(maxArea, s[0][0] * s[0][1] + s[1][0] * s[1][1])
  # 90도 돌렸을 때
  if s[0][1] <= H and s[1][0] <= H:
    if s[0][0] + s[1][1] <= W:
      maxArea = max(maxArea, s[0][0] * s[0][1] + s[1][0] * s[1][1])
  # 둘다 90도 돌렸을 때
  if s[0][1] <= H and s[1][1] <= H:
    if s[0][0] + s[1][0] <= W:
      maxArea = max(maxArea, s[0][0] * s[0][1] + s[1][0] * s[1][1])
      
  # 세로로 2개 붙이는 경우
  # 가로 길이가 일단 W보다 작아야 하므로
  if s[0][1] <= W and s[1][1] <= W:
    if s[0][0] + s[1][0] <= H:
      maxArea = max(maxArea, s[0][0] * s[0][1] + s[1][0] * s[1][1])
  # 90도 돌렸을 때
  if s[0][1] <= W and s[1][0] <= W:
    if s[0][0] + s[1][1] <= H:
      maxArea = max(maxArea, s[0][0] * s[0][1] + s[1][0] * s[1][1])
  # 90도 돌렸을 때
  if s[0][0] <= W and s[1][1] <= W:
    if s[0][1] + s[1][0] <= H:
      maxArea = max(maxArea, s[0][0] * s[0][1] + s[1][0] * s[1][1])
  # 둘다 90도 돌렸을 때
  if s[0][0] <= W and s[1][0] <= W:
    if s[0][1] + s[1][1] <= H:
      maxArea = max(maxArea, s[0][0] * s[0][1] + s[1][0] * s[1][1])
      
print(maxArea)