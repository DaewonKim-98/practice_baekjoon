# dfs를 통해 최소 금액 찾기
# 아 시간초과 이거 다이스트라인가 아오
import heapq
import sys
input = sys.stdin.readline
dir = ((0, 1), (1, 0), (0, -1), (-1, 0))

def go_exit(r, c):
    visited = [[0] * N for _ in range(N)]
    heap = []
    heapq.heappush(heap, (arr[0][0], r, c))
    
    while heap:
        rupee, r, c = heapq.heappop(heap)
        if visited[r][c] == 0:
            visited[r][c] = rupee
            if r == N - 1 and c == N - 1:
                return rupee
            
            for d in dir:
                nr, nc = r + d[0], c + d[1]
                if 0 <= nr < N and 0 <= nc < N:
                    # 가는 길에서 가장 적은 소지금을 계속 갱신하면서 하면
                    # 중복을 더 방지할 수 있나
                    if min_cost[nr][nc] > visited[r][c] + arr[nr][nc]:
                        min_cost[nr][nc] = visited[r][c] + arr[nr][nc]
                        heapq.heappush(heap, (visited[r][c] + arr[nr][nc], nr, nc))

i = 0
while True:
    i += 1
    N = int(input().strip())
    if N == 0:
        exit()
    arr = [list(map(int, input().strip().split())) for _ in range(N)]
    min_cost = [[9 * N * N] * N for _ in range(N)]
    
    print(f'Problem {i}: {go_exit(0, 0)}')