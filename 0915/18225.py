import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input().strip())
arr = [int(input().strip()) for _ in range(N)]
lst = [0] * 8001

s = sum(arr)
# 첫번째는 산술평균
first = round(s / N)
arr.sort()
# 두번째는 중앙값
second = arr[N // 2]
for i in arr:
    lst[i] += 1

# 최빈값 카운트
m = max(lst)
cnt = 0
for i in range(4001, 8001):
    if lst[i] == m:
        cnt += 1
        third = i - 8000 - 1
        # 두번째로 작은 값이 나오면 출력
        if cnt == 2:
            third = i - 8000 - 1
            break
# break이 안났으면 아직 두번째 최빈값을 찾지 못했다는 것이므로
# 한번 더 for문 돌리기
else:
    for i in range(0, 4001):
        if lst[i] == m:
            cnt += 1
            third = i
            # 두번째로 작은 값이 나오면 출력
            if cnt == 2:
                third = i
                break

forth = arr[-1] - arr[0]

print(first)
print(second)
print(third)
print(forth)