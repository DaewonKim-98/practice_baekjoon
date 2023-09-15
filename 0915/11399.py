import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input().strip())
arr = list(map(int, input().split()))

# 전체의 합이 최소가 되려면 작은 수부터 만들어서 더하면 되므로
arr.sort()
# 누적합 사용으로 시간 줄이기
lst = [0] * N
lst[0] = arr[0]
for i in range(1, N):
    lst[i] = lst[i - 1] + arr[i]

print(sum(lst))