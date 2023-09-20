import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 절단기의 최대 높이는 arr의 최대 높이
l = 0
r = max(arr)

# 이분탐색
while l <= r:
    # 절단기의 높이
    middle = (l + r) // 2
    # 가져가는 나무
    tree = 0
    for i in arr:
        # 절단기보다 나무의 높이가 높아야 나무를 가져가므로
        if middle < i:
            tree += (i - middle)

    # 가져가는 나무가 M보다 항상 크거나 같아야 하므로
    if M <= tree:
        l = middle + 1
    # 가져가는 나무가 M보다 작으면 절단기 높이 낮추기
    else:
        r = middle - 1

print(r)