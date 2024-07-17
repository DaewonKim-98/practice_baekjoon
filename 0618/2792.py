import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
arr = [int(input().strip()) for _ in range(M)]

# 최소가 되는 질투심 이분탐색으로 찾기
start = 1
end = max(arr)

while start <= end:
    mid = (start + end) // 2
    people = 0
    # 질투심을 보석에서 나눈만큼 아이들에게 줄 수 있으므로
    for i in arr:
        if i % mid == 0:
            people += i // mid
        else:
            people += i // mid + 1
    # print(mid, people)
    if people > N:
        start = mid + 1
    else:
        end = mid - 1
print(start)