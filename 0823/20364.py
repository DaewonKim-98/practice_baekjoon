import sys
from collections import deque
input = sys.stdin.readline

N, Q = map(int, input().split())

# 점유된 땅 리스트
visited_land = set()
for i in range(Q):
    duck = int(input().strip())
    land = duck
    # 처음 점유된 땅을 0으로 두고 시작
    visited = 0
    # 땅이 0이 될 때까지 반복
    while land > 0:
        # 만약 땅이 점유된 곳에 있으면
        if land in visited_land:
            # 출력할 점유된 땅을 계속 갱신
            visited = land
        # 부모 노드를 찾기
        land = land // 2
    # 만약 점유된 땅의 최솟값이 점유 된 땅 리스트에 있으면
    if visited in visited_land:
        print(visited)
    # 다 돌려도 괜찮았으면 땅을 점유할 수 있으므로
    else:
        print(visited)
        visited_land.add(duck)