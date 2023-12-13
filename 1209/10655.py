N = int(input())

min_distance = 2000
distance = 0
point = []
for i in range(N):
    x, y = map(int, input().split())
    point.append([x, y])
    if 3 <= i < N:
        distance += abs(point[i - 2][0] - point[i - 3][0]) + abs(point[i - 2][1] - point[i - 3][1])
    if 2 <= i < N:
        min_distance = min(min_distance + abs(x - point[i - 1][0]) + abs(y - point[i - 1][1]),
                           distance + abs(x - point[i - 2][0]) + abs(y - point[i - 2][1]))

print(min_distance)