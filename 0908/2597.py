N = int(input())
red1, red2 = map(int, input().split())
blue1, blue2 = map(int, input().split())
yellow1, yellow2= map(int, input().split())

# 빨간 점 먼저 접기
# 중심
red_center = (red1 + red2) / 2
# 줄자 길이 갱신
N = max(red_center, N - red_center)

# 파란 점 위치 갱신
if blue1 <= red_center:
    blue1 = red_center - blue1
else:
    blue1 = blue1 - red_center

if blue2 <= red_center:
    blue2 = red_center - blue2
else:
    blue2 = blue2 - red_center

# 파란 점 접기
# 만약 두 파란 점이 같으면 두 점이 이미 만나는 것이므로
if blue1 == blue2:
    blue_center = red_center
else:
    blue_center = (blue1 + blue2) / 2
    # 줄자 길이 갱신
    N = max(blue_center, N - blue_center)

# 노란 점 위치 갱신
if yellow1 <= red_center:
    yellow1 = red_center - yellow1
else:
    yellow1 = yellow1 - red_center

if yellow2 <= red_center:
    yellow2 = red_center - yellow2
else:
    yellow2 = yellow2 - red_center

# 노란 점 위치 갱신
if yellow1 <= blue_center:
    yellow1 = blue_center - yellow1
else:
    yellow1 = yellow1 - blue_center

if yellow2 <= blue_center:
    yellow2 = blue_center - yellow2
else:
    yellow2 = yellow2 - blue_center

# 노란 점 접기
# 만약 두 노란 점이 같으면 두 점이 이미 만나는 것이므로
if yellow1 == yellow2:
    yellow_center = blue_center
else:
    yellow_center = (yellow1 + yellow2) / 2
    # 줄자 길이 갱신
    N = max(yellow_center, N - yellow_center)

print(f'{N:.1f}')