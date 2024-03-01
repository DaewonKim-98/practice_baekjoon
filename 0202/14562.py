from collections import deque

def bfs(i):
  q = deque()
  # 점수, 발차기 횟수, A를 했을 때 상대가 3점 득점 더 하므로 그만큼 +점수
  q.append((i, 0, 0))

  while q:
    i, cnt, plus = q.popleft()
    # T랑 만나면
    if i == T + plus:
      print(cnt)
      return
    
    q.append((i + 1, cnt + 1, plus))
    if i * 2 <= T + plus + 3:
      q.append((i * 2, cnt + 1, plus + 3))

C = int(input())

# 윤예빈때문에 dp로 풀다가 시간 다 뿌셔질뻔 했다 크헝헝헝헝헝헝헝허엏엏ㅇ
for _ in range(C):
  S, T = map(int, input().split())
  
  bfs(S)