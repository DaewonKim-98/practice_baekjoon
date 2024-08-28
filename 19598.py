import sys
import heapq
input = sys.stdin.readline

N = int(input().strip())

meetings = [tuple(list(map(int, input().strip().split()))) for _ in range(N)]
meetings.sort()

# 회의 끝나는 시간을 heap에 저장 후 시작 시간과 비교해서 가장 빨리 끝나는 시간보다
# 시작 시작이 빠르면 새로운 회의, 아니면 회의 다음 바로 회의
overMeeting = [meetings[0][1]]
heapq.heapify(overMeeting)

for i in range(1, N):
    minOverTime = heapq.heappop(overMeeting)
    if meetings[i][0] >= minOverTime:
        heapq.heappush(overMeeting, meetings[i][1])
    else:
        heapq.heappush(overMeeting, minOverTime)
        heapq.heappush(overMeeting, meetings[i][1])

print(len(overMeeting))