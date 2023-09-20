import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, C = map(int, input().split())
x = [int(input()) for _ in range(N)]
x.sort()

# 최소 거리, 최대 거리
l = 1
r = x[-1] - x[0]

# 인접한 두 공유기 사이의 최대 거리
while l <= r:
    # 두 공유기 사이의 거리
    middle = (l + r) // 2
    # 설치하는 공유기의 갯수와 공유기가 설치된 집
    cnt = 1
    house = x[0]
    # 집에서 공유기 사이의 거리를 더한게 다음 집보다 작거나 같으면 설치가 가능하다는 것이므로
    for i in range(N):
        if house + middle <= x[i]:
            cnt += 1
            house = x[i]
    # 설치하려는 공유기의 개수가 C보다 크거나 같으면 거리를 최대한 늘려보기
    if cnt >= C:
        l = middle + 1
    # 설치하려는 공유기의 개수가 C보다 작으면 거리를 줄여 설치를 가능하게
    else:
        r = middle - 1

print(r)