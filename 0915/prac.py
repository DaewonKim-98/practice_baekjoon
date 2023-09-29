import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input().strip())

arr = [list(map(int, input().split())) for _ in range(N)]

# 끝나는 시간대로 정렬한 수 시작하는 시간대로 정렬
print(arr)
arr.sort(key=lambda x: x[1])
print(arr)
arr.sort(key=lambda x: x[0])
print(arr)

# 끝나는 시간과 시작하는 시간을 매치해서 회의의 개수 카운트
cnt = 1
# 마지막 회의의 시작하는 시간
last = arr[N - 1][0]
for i in range(N - 2, -1, -1):
    # 끝나는 시간은 다음 회의 시간의 시작하는 시간보다 빠르거나 같아야하므로
    if arr[i][1] <= last:
        cnt += 1
        last = arr[i][0]

print(cnt)