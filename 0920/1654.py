import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

K, N = map(int, input().split())
arr = [int(input().strip()) for _ in range(K)]

# 만약 전체 한 줄일 때 만들 수 있는 최대 길이는
max_lenth = sum(arr) // N

# 이진 탐색으로 찾기?
l = 1
r = max_lenth

while l <= r:
    middle = (l + r) // 2
    sum_len = 0
    # 만약 랜선 수의 합이 N보다 크거나 같을 때 계속 l을 갱신
    for i in arr:
        sum_len += i // middle
    if sum_len >= N:
        l = middle + 1
    elif sum_len < N:
        r = middle - 1
print(r)
