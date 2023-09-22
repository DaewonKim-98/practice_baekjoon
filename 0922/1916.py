import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import heapq

def price(sp, ep):
    visited = [0] * (N + 1)
    heap = []
    heapq.heappush(heap, (0, sp))

    # 힙이 있는 동안 계속 반복
    while heap:
        price, sp = heapq.heappop(heap)
        # 방문하지 않은 곳이면
        if visited[sp] == 0:
            # 방문처리
            visited[sp] = 1
            # 도착점이라면 최솟값 출력
            if sp == ep:
                return price
            # startpoint가 갈 수 있는 곳을 탐색
            for p, e in M_list[sp]:
                if visited[e] == 0:
                    heapq.heappush(heap, (price + p, e))

N = int(input().strip())
M = int(input().strip())

M_list = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, p = map(int, input().split())
    M_list[s].append([p, e])

sp, ep = map(int, input().split())

print(price(sp, ep))
