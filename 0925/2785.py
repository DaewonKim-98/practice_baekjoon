import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

N = int(input().strip())
arr = deque(map(int, input().split()))

# N이 2일 때는 무조건 1이 최소이므로
if N == 2:
    print(1)
# 3 이상일 때는 가장 작은 수부터 없애면서 큰 수들 사이에 하나씩 고리를 끼워넣어 연결해준다는
# 생각으로 하면 그 사이가 더 이상 없을 때가 필요한 고리의 최소의 수 일 듯?
else:
    arr = sorted(arr)
    arr = deque(arr)
    # 더 이상 고리가 남지 않을 때까지 최솟값과 고리들을 제거
    cnt = 0
    while len(arr) > 0:
        min_val = arr.popleft()
        # 사이사이에 고리들을 넣은 것이므로 그 만큼을 제거
        for _ in range(min_val):
            if len(arr) == 0:
                break
            arr.pop()
            cnt += 1

    print(cnt)

    
