import heapq

def bfs(i):
  num = 0
  q = []
  heapq.heappush(q, (0, 0))
  
  while q:
    sum, cnt = heapq.heappop(q)
    # print(sum, cnt)
    # i가 num + 1이면 num+1 근데 num + 1보다 크면 중간에 띄워지는 것이므로 끝
    if sum == num + 1:
      num += 1
    elif sum > num + 1:
      if num % 2 == 0:
        print(f'jjaksoon win at {num + 1}')
        return
      else:
        print(f'holsoon win at {num + 1}')
        return
    for j in range(N):
      if cnt < K:
        if visited[sum + arr[j]] == 0:
          heapq.heappush(q, (sum + arr[j], cnt + 1))
          visited[sum + arr[j]] = 1
        


N = int(input())
arr = list(map(int, input().split()))
K = int(input())

# bfs를 통해
visited = [0] * 50001
bfs(0)