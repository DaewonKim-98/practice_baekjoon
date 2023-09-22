import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

# 방향
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

def miro(sp, ep):
    r, c = sp
    visited = [[0] * (N) for _ in range(N)]
    heap = []
    heapq.heappush(heap, (0, r, c))

    # 힙이 있는 동안 반복
    while heap:
        v, r, c = heapq.heappop(heap)
        # 방문하지 않았다면
        if visited[r][c] == 0:
            # 방문 표시
            visited[r][c] = 1
            # 끝방에 도착했다면 방 수 출력
            if r == ep[0] and c == ep[1]:
                return v 
            for d in dir:
                nr, nc = r + d[0], c + d[1]
                if 0 <= nr < N and 0 <= nc < N:
                    # 방문하지 않았다면
                    if visited[nr][nc] == 0:
                        heapq.heappush(heap, (v + 1 - arr[nr][nc], nr, nc))


N = int(input())
arr = [list(map(int, input().strip())) for _ in range(N)]

sp, ep = (0, 0), (N - 1, N - 1)

print(miro(sp, ep))