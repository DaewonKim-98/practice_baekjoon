# 나는 개똥벌레 친구가 없네 저기 개똥 무덤이 내 집인걸
# 아무리 우겨봐도 친구가 없네 

import sys
input = sys.stdin.readline

N, H = map(int, input().strip().split())
arr = [int(input().strip()) for _ in range(N)]

# 각 구간별 장애물의 개수를 나타내는 리스트
obstacleList = [0] * (H + 1)
  
for i in range(N):
  # 석순이면 밑에서부터하는데 나중에 누적합으로 계산하기 위해 1은 무조건 포함되므로
  # 1더해주고 끝 + 1에 -1 해주기
  if i % 2 == 0:
    obstacleList[1] += 1
    obstacleList[arr[i] + 1] -= 1
  # 종유석이면 거꾸로이므로 걍 밑에서 시작점에서 +1
  else:
    obstacleList[H - arr[i] + 1] += 1
    
# 누적합으로 ㄹㅇ 장애물 개수 찾기
for i in range(1, H + 1):
  obstacleList[i] = obstacleList[i - 1] + obstacleList[i]
  
obstacleList.pop(0)

print(min(obstacleList), obstacleList.count(min(obstacleList)))