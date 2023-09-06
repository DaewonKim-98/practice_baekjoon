import sys
input = sys.stdin.readline

N = int(input().strip())
arr = [0] + [int(input().strip()) for _ in range(N)]

lst = [0] * (N + 2)

if N == 1:
    print(arr[1])

else:

    lst[1] = arr[1]
    lst[2] = arr[1] + arr[2]

    # 최댓값은 연속해서 마시면 안된다는걸 생각해서 앞과 앞앞을 생각한다.
    for i in range(3, N + 1):
        lst[i] = max(lst[i - 2] + arr[i], lst[i - 3] + arr[i - 1] + arr[i], lst[i - 1])

    print(lst[N])