import sys
import heapq
input = sys.stdin.readline

def goMasanDirect(i):
    global minLength
    global gunLength
    visited = [0] * (V + 1)
    q = []
    heapq.heapify(q)
    heapq.heappush(q, (0, 1))
    
    while q:
        length, i = heapq.heappop(q)
        # 마산에 도착하면
        if i == V:
            minLength = length
            return
        if visited[i] == 0:
            # 건우에 도착하면
            if i == P:
                gunLength = length
            visited[i] = 1
            for j in link[i]:
                heapq.heappush(q, (length + j[0], j[1]))
                
def throughGun(i):
    global minLength
    global gunLength
    l = 0
    visited = [0] * (V + 1)
    q = []
    heapq.heapify(q)
    heapq.heappush(q, (gunLength, P))
    
    while q:
        length, i = heapq.heappop(q)
        # 다시 마산에 도착하면 끝
        if i == V:
            if minLength == length:
                print('SAVE HIM')
            else:
                print('GOOD BYE')
            return
        if visited[i] == 0:
            visited[i] = 1
            for j in link[i]:
                heapq.heappush(q, (length + j[0], j[1]))

V, E, P = map(int, input().strip().split())
link = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b, c = map(int, input().strip().split())
    link[a].append((c, b))
    link[b].append((c, a))
# print(link)   
# 다이스트라
minLength = 0
gunLength = 0
goMasanDirect(1)
# 건우를 거치고 간게 mimLength와 똑같으면 우정을 지킴
throughGun(1)