import sys
input = sys.stdin.readline

# 타일 까는걸 생각하면 N 개일 때 N - 2개의 가짓수에서 00을 추가하거나 N - 1 개의 가짓수에서 1을 추가한
# 것이 전체 가짓수가 된다고 생각할 수 있으므로
def tile(N):
    # 1개와 2개일 때의 경우
    arr[1] = 1
    arr[2] = 2
    if N > 2:
        for i in range(3, N + 1):
            arr[i] = arr[i - 2] + arr[i - 1]
    return arr[N]

N = int(input().strip())
arr = [0] * 1000001
result = tile(N) % 15746
print(result)


# # 조합 함수
# def c(n, r):
#     result = 1
#     for i in range(n, n - r, -1):
#         result *= i
#     for j in range(1, r + 1):
#         result //= j
#     return result

# arr = ['00', '1']

# # 만들 수 있는 가짓수는 nC0 + (n -1)N1 + ....
# k = 0
# cnt = 0
# while k <= N:
#     cnt += c(N, k)
#     N -= 1
#     k += 1
# print(cnt)