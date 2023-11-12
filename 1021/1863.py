N = int(input())
# 건물 개수
cnt = 0
# 아놔 진짜 왜틀리지 다시 시작해보자
# 스카이라인이 올라갈 때마다 새로운 건물이 추가되는데, 스카이라인이 줄어들었을 때
# 추가했던 건물보다 높이가 작거나 같게 되면 그때까지 건물을 세주기로 바꾸자
high = [0]
for _ in range(N):
    x, y = map(int, input().split())
    next = y
    # 가장 뒤에 건물보다 높이가 작게 되면 그거 빼면서 개수 추가
    while high[-1] > y:
        if high[-1] != next:
            cnt += 1
        next = high.pop()
    # 건물 추가
    high.append(y)

next = 0
# 가장 뒤에 건물보다 높이가 작게 되면 그거 빼면서 개수 추가
while high[-1] > 0:
    if high[-1] != next:
        cnt += 1
    next = high.pop()

  
print(cnt)