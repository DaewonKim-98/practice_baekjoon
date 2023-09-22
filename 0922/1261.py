import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# 방향
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def algospot(sp, ep):
    visited = [[0] * (M) for _ in range(N)]
    r, c = sp
    heap = []
    heapq.heappush(heap, (0, r, c))

    # 힙이 있는 동안 실행
    while heap:
        v, r, c = heapq.heappop(heap)
        # 방문하지 않았으면
        if visited[r][c] == 0:
            # 방문 표시
            visited[r][c] = 1
            # N, M에 도착한다면
            if r == ep[0] and c == ep[1]:
                return v
            for d in dir:
                nr, nc = r + d[0], c + d[1]
                if 0 <= nr < N and 0 <= nc < M:
                    if visited[nr][nc] == 0:
                        heapq.heappush(heap, (v + arr[nr][nc], nr, nc))

M, N = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]

sp, ep = (0, 0), (N - 1, M - 1)

print(algospot(sp, ep))