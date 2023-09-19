import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

K, N = map(int, input().split())
arr = [int(input().strip()) for _ in range(K)]

# 만약 전체 한 줄일 때 만들 수 있는 최대 길이는
max_lenth = sum(arr) // N
# 최소 길이는
min_length = 0
for i in arr:
    min_length += i // N
print(min_length)

# 이진 탐색으로 찾기?
l = 1
r = max_lenth
# 딱 K로 나누어떨어지지 않으면
result = False
while l <= r:
    middle = (l + r) // 2
    sum_len = 0
    # 만약 랜선 길이의 합이 N가 된다면 
    for i in arr:
        sum_len += i // middle
    if sum_len == N:
        # 최댓값을 찾아야하므로 그대로 N일 동안 계속 middle을 1씩 올리기
        while sum_len == N:
            middle += 1
            sum_len = 0
            # 만약 랜선 길이의 합이 N가 된다면 
            for i in arr:
                sum_len += i // middle
            result = True
        print(middle - 1)
        break
    elif sum_len < N:
        r = middle - 1
    else:
        l = middle + 1

# 딱 K로 나누어떨어지지 않으면 K보다 크게 만들어도 된다고 했으므로
if result == False:
    while True:
        sum_len = 0
        # 만약 랜선 길이의 합이 N가 된다면 
        for i in arr:
            sum_len += i // middle
        if sum_len >= N:
            print(middle)
            break
        middle -= 1

