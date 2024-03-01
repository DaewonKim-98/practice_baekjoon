R, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
T = int(input())

# 필터링 이미지
img = [[0] * (C - 2) for _ in range(R - 2)]

# arr을 돌면서 중앙값 찾고 필터링 이미지에 추가
for r in range(R - 2):
    for c in range(C - 2):
        numbers = []
        for i in range(3):
            for j in range(3):
                numbers.append(arr[r + i][c + j])
        numbers.sort()

        img[r][c] = numbers[4]
        
# 필터링 이미지 중 T보다 큰 것들
cnt = 0
for r in range(R - 2):
    for c in range(C - 2):
        if img[r][c] >= T:
            cnt += 1
            
print(cnt)