import sys
from collections import deque
input = sys.stdin.readline

N, Q = map(int, input().split())

# 점유된 땅 리스트
visited_land = set()
for i in range(Q):
    duck = int(input().strip())
    land = duck
    visited = 0
    while land > 0:
        if land in visited_land:
            visited = land
        land = land // 2
    if visited in visited_land:
        print(visited)
    # 다 돌려도 괜찮았으면 땅을 점유할 수 있으므로
    else:
        print(visited)
        visited_land.add(duck)