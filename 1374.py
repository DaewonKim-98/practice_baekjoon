import sys
import heapq
input = sys.stdin.readline

N = int(input().strip())
arr = [list(map(int, input().strip().split())) for _ in range(N)]
arr.sort(key=lambda x: [x[1], x[2]])

# 힙으로 정렬해서 가장 앞에 있는 강의 종료 시간과 비교
# 가장 종료 시간보다 시작 시간이 더 빠르면 새로 강의 생성
room = []
heapq.heappush(room, arr[0][2])
for i in range(1, N):
    # 시작 시간이 더 빠르면 추가
    if arr[i][1] < room[0]:
        heapq.heappush(room, arr[i][2])
    # 더 느리면 강의 이어서
    else:
        heapq.heappushpop(room, arr[i][2])
        
print(len(room))