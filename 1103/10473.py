import heapq
import math

# 두 점 사이의 거리
def distance(start, end):
    return math.sqrt((start[0] - end[0]) ** 2 + (start[1] - end[1]) ** 2)

def run(i):
    global min_time
    visited = [0] * (N + 2)
    heap = []
    heapq.heappush(heap, i)

    while heap:
        lst = heapq.heappop(heap)
        # 마지막에 도착했으면 최솟값 갱신
        if lst[1] == N + 1:
            if min_time > lst[0]:
                min_time = lst[0]
            return
        # 방문한 곳이 아니면
        if visited[lst[1]] == 0:
            visited[lst[1]] = 1

            for j in n_list[lst[1]]:
                heapq.heappush(heap, (j[0] + lst[0], j[1]))


start = [tuple(map(float, input().split()))]
end = [tuple(map(float, input().split()))]

N = int(input())

# 처음과 끝을 포함해 모든 점들을 연결한 간선 리스트를 만들고 그 간선리스트는 각각 가는 시간들을 가지고 있음
arr = []
for _ in range(N):
    arr.append(tuple(map(float, input().split())))

arr = start + arr + end
# print(arr)
# 각 대포들과 출발지, 도착지를 모두 연결했고 그까지 가는 거리들을 함께 간선 리스트에 포함
n_list = [[] for _ in range(N + 2)]
for i in range(N + 2):
    for j in range(N + 2):
        if i != j:
            # 출발지점에서는 대포로 걸어갈 수밖에 없으므로
            if i == 0:
                n_list[i].append((distance(arr[i], arr[j]) / 5, j))
            # 마지막 지점은 대포타고 가는 것과 걸어가는 것 중에서 최솟값
            elif i == N + 1:
                if distance(arr[i], arr[j]) >= 50:
                    n_list[i].append(((distance(arr[i], arr[j]) - 50) / 5 + 2, j))
                else:
                    n_list[i].append((min(2 + (50 - distance(arr[i], arr[j])) / 5, distance(arr[i], arr[j]) / 5), j))
            # 나머지는 대포타고 가는 것과 걸어가는 것 중에서 최솟값
            else:
                if distance(arr[i], arr[j]) >= 50:
                    n_list[i].append(((distance(arr[i], arr[j]) - 50) / 5 + 2, j))
                else:
                    n_list[i].append((min(2 + (50 - distance(arr[i], arr[j])) / 5, distance(arr[i], arr[j]) / 5), j))

# print(n_list)
# 시작점부터 시간에 대해 다이스트라
min_time = 200
for i in n_list[0]:
    run(i)

print(min_time)