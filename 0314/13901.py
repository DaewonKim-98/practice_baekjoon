R, C = map(int, input().split())
k = int(input())
arr = [[0] * C for _ in range(R)]
# 장애물 표시
for _ in range(k):
  r, c = map(int, input().split())
  arr[r][c] = -1
# 시작 위치 표시
sr, sc = map(int, input().split())
arr[sr][sc] = 1

dir = {
  1: [-1, 0], 
  2: [1, 0], 
  3: [0, -1],
  4: [0, 1]
}
dirSequence = list(map(int, input().split()))
# 못움직일 때까지 계속 움직여라
i = 0
dirCnt = 0
while True:
  nr, nc = sr + dir[dirSequence[i]][0], sc + dir[dirSequence[i]][1]
  # 움직일 수 있으면
  if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] == 0:
    arr[nr][nc] = 1
    dirCnt = 0
    sr, sc = nr, nc
  # 못 움직이면 i 추가
  else:
    # 만약 dirCnt가 len(dirSequence)가 된다면 모든 방향으로 못 움직인다는 것이므로
    if dirCnt == len(dirSequence):
      break
    i += 1
    i %= len(dirSequence)
    dirCnt += 1
    
print(sr, sc)