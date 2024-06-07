from collections import deque

def bfs(i):
  # 이모티콘 개수 클립 ㅁㄴ앎ㄴㅇㅎㅁㄴㅇㄻㅇ뢰;낭로함얼훎ㄴ일허ㅏㅁㅇ루ㅏㅓㅎ
  visited = [[0] * 2001 for _ in range(2001)]
  q = deque()
  # 이모티콘 개수, 클립
  q.append((i, 1))
  
  while q:
    i, clip = q.popleft()
    if i == S:
      print(visited[i][clip])
      return
    
    # 클립보드에 복사
    if visited[i][i] == 0:
      q.append((i, i))
      visited[i][i] = visited[i][clip] + 1
      
    # 클립보드에 있는거 추가
    if 0 <= i + clip < 2001 and visited[i + clip][clip] == 0:
      q.append((i + clip, clip))
      visited[i + clip][clip] = visited[i][clip] + 1

    # 하나 삭제
    if 2 <= i - 1 < 2001 and visited[i - 1][1] == 0:
      q.append((i - 1, clip))
      visited[i - 1][clip] = visited[i][clip] + 1
    
S = int(input())

# bfs를 통해
bfs(1)